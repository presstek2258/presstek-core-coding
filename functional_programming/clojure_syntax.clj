; if else form
(println (if (< 1 2) "true" "false"))

;cond form 
(def age 45)
(cond (< age 12) "go have fun"
      (< age 16) "maybe have fun"
      :else "dont go")

; iteration using the for-form
; needs bindings 
; the bindings is in vector form
; this returns a sequence!!!
; input sequence length = output sequence length
(range 10)
(for [x (range 10)] (* x x))

;nested
; [x y] just returns pairs
(for [x (range 10)
      y (range 10)]
  [x y])

;add a condition
;when x + y > 7
(for [x (range 10)
      y (range 10)
      :when (> (+ x y) 7)]
  [x y])

; iterate through hashmap
; why do we get nil? 3 times
; jupyter kernel returns nil from a for loop
; this wont occur outside jupyter
(for [x {:age 50
         :name "albert "
         :hobbies "physics "}]
  (println "key is " (x 0) "value is " (x 1)))

;you can prevent/ suppress this with a ; at the end 
;this will print nil
(println "hey");
;this wont print nil
(println "hey")

; do blocks
(do (print "o") (print "k"));
; do all just ensure everything gets run
(doall (print "o") (print "k\n"));

;the let-form
(let [name "albert"
      hobby :physics]
  (str "name is " name " with hobby " :hobby))

;(str "what is hobby now?" hobby)
; error will happen because there is no symbol binding for hobby

;can use def to define things
;even functions
;(it might be better to use defn though if its a function)
(def areaSquare (fn [length] (* length length)))
(println (areaSquare 5))

;recursion stuff fibonacci
;find fib(500)
;warning stack overflow
;no tail recursion
(defn fib [n]
  (case n
    0 1
    1 1
    (+ (fib (- n 1)) (fib (- n 2)))))

; not for wont execute the whats in the body
; this wont print anything
(for [x (range 10)] (println (+ x x)))
;need to use do instead
;doseq is do but for sequences
(doseq [x (range 10)] (println "fib" x ": " (fib x)))

;sum up the values from a vector
;using loop and recur sum up the values from a vector
;when using loop recur is called to increment the loop
(def values [3 4 2])
(println "sum: " (loop [i 0
                        sum 0]
                   (cond
                     (= i (count values)) sum
                     :otherwise (recur (inc i) (+ sum (values i))))))
; a much faster was to get the sum is with apply 
(println "apply sum: " (apply + values))

;fibonacci with tail recursion
;todo: not working yet
;todo: recursion video
(defn fib [n]
  (cond
    (= n 0) 1
    (= n 1) 1
    :otherwise
    (loop [i 2
           last-2 [1 1]]
      (let [i-th-fib (apply + last-2)]
        (if (= i n)
          i-th-fib
          (recur (inc i) [(last last-2) i-th-fib]))))))

;test with large fib values
(println (fib 10))
(println (fib 20))
(println (fib 30))
