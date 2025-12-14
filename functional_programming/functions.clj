; compute to console the first 20 factorials
(defn fac [n]
  (apply * (rest (range (+ n 1)))))

; (doall (for [i (range 20)]
;          (println (fac i))))

; write fibonacci sequence with 
(defn fib [n]
  (if (<= n 1)
    1
    (+ (fib (- n 1)) (fib (- n 2)))))

; (doall (for [i (range 10)]
;          (println (fib i))))

;make an includes method that checks for and element
;do this with both filter, for, and loop-recur

(defn includes? [n arr]
  (not (empty? (filter (fn [e] (= e n)) arr))))

(defn includes? [n arr]
  (loop [arr arr]
    (cond
      (empty? arr) false
      (= n (first arr)) true
      :else (recur (rest arr)))))

(defn includes? [n arr]
  (not (empty?
        (for [e arr :when (= e n)] e))))

; (println (includes? :a [:a :b :c]))
; (println (includes? :i [:a :b :c]))

; create a function intersect that prints the elements in both vectors
; do it 2 ways. with for and with filter

(defn intersect [arr1 arr2]
  (for [x arr1 y arr2 :when (= x y)] x))

(defn intersect [arr1 arr2]
  (filter (fn [x] (includes? x arr2)) arr1))

(println (intersect [:a :b :c] [:b :c :d :e]))

;get the averages of each student ["name" average]
;answer: (["Jack" 74.75] ["Joe" 78.5] ["Jill" 88.0])
(def students [{:name "Jack"
                :age 45
                :grades {:english 80 :math 76 :biology 55 :cs 88}}
               {:name "Joe"
                :age 20
                :grades {:english 90 :math 77 :cs 80 :biology 67}}
               {:name "Jill"
                :age 21
                :grades {:math 89 :cs 97 :biology 79 :english 87}}])

(defn get-student-averages [students]
  (for [student students]
    [(get student :name)
     (double (/ (apply + (vals (get student :grades))) 4))]))

(println "average grades\n" (get-student-averages students))

;challenge find the lowest grade for each student
(defn get-lowest-grade [students]
  (for [student students]
    (loop [sgrades (vals (get student :grades))
           mingrade 100]
      (if (empty? sgrades)
        [(get student :name) mingrade]
        (recur (rest sgrades) (if (< (first sgrades) mingrade)
                                (first sgrades)
                                mingrade))))))

(println "lowest grades\n" (get-lowest-grade students))

;see if there is an optimization with min 
(defn get-lowest-grade-min [students]
  (for [student students]
    [(get student :name)
     (min (vals (get student :grades)))]))

(println "lowest grades with min \n" (get-lowest-grade students))
