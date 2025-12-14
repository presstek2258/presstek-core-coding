(require '[clojure.java.io :as io])

; split a string into a vector
(defn split-string [s]
  (loop [i 0
         acc []
         word ""]
    (if (= i (count s))
      (conj acc word)
      (recur (inc i) ;i
             (if (= (get s i) \,) ;acc
               (conj acc word)
               acc)
             (if (= (get s i) \,) ;word
               ""
               (str word (get s i)))))))

(def string "first,second,third")
(def res (split-string string))
(println res)
(println (get res 2))

;next check if a string can be double, or long 
;convert if it can
(defn parse-value [string datatype]
  (cond
    (= :str datatype) string
    (= :double datatype) (parse-double string)
    (= :int datatype) (parse-long string)
    :else
    (do (println "error cannot parse")
        nil)))


; used for next function
(def columns
  [[:id :str]
   [:attrition :str]
   [:age :int]
   [:gender :str]
   [:dependents :int]
   [:education :str]
   [:marital :str]
   [:income :str]
   [:card :str]
   [:months :int]
   [:rel-count :int]
   [:inactive :int]
   [:contacts :int]
   [:limit :double]
   [:balance :double]
   [:open :int]
   [:change :double]
   [:amount :double]
   [:count :double]
   [:change2 :double]
   [:ratio :double]])

; function for taking a string line and 
; making it into a dictionary
(defn make-record [line]
  (def arr (split-string line)) ;split into vector 
  (loop [i 0
         hmap {}]

    (if (< i (count columns))
      (recur (inc i)
             (assoc hmap
                             ;key
                    (first (get columns i))
                             ;value
                    (parse-value (get arr i) (last (get columns i)))))
      hmap)))

; returns a hashmap with total count and total limit, 
; and # of records
(defn total-count-limit [lines]
  (let [veclines (vec lines)];change input into vector
    (loop [i 0
           hmap {:total-count 0
                 :total-limit 0
                 :count 0}]

      (if (< i (count veclines))
        (let [record (make-record (get veclines i))]
          (recur (inc i)
                 (assoc hmap
                        :total-count ;key
                        (+ (:total-count hmap)
                           (:count record)) ;value

                        :total-limit ;key
                        (+ (:total-limit hmap)
                           (:limit record)) ;value

                        :count ;key
                        (inc (:count hmap)) ;value
                        )))
        hmap))))

; returns a hashmap with the average count and average limit
(defn average-count-limit [lines]
  (let [veclines (vec lines)];change input into vector
    (loop [i 0
           hmap {}
           sum-count 0
           sum-limit 0]

      (if (< i (count veclines))
        (let [record (make-record (get veclines i))]
          (recur (inc i)
                 hmap
                 (+ sum-count (:count record))
                 (+ sum-limit (:limit record))))

        (assoc hmap
               :average-count ;key
               (/ sum-count i) ;value
               :average-limit ;key
               (/ sum-limit i)))))) ;value


; TESTING: check function outputs with dataset
(println (parse-value "324" :int))
(println (parse-value "hey" :str))
(println (parse-value "324" :double))
(println (parse-value "asd" :double))
(println "")
;
; load the csv to test the functions
(def CSV-FILE "./BankChurners.csv")
; load the lines from the file
(def lines 
    (with-open [rdr (io/reader CSV-FILE)]
                (into [] (line-seq rdr))))

; show an example record
(println (make-record (second lines)))
(println "")
; take 10 records as an example
(println(total-count-limit (take 10 (rest lines))))
(println "")
; take the average count of the records
(println(average-count-limit (rest lines)))
(println "")
