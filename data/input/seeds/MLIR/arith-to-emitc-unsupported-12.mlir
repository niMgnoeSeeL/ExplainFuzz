"builtin.module"() ({
  "func.func"() <{function_type = (vector<5xf32>) -> vector<5xf32>, sym_name = "arith_negf_vector"}> ({
  ^bb0(%arg0: vector<5xf32>):
    %0 = "arith.negf"(%arg0) <{fastmath = #arith.fastmath<none>}> : (vector<5xf32>) -> vector<5xf32>
    "func.return"(%0) : (vector<5xf32>) -> ()
  }) : () -> ()
}) : () -> ()

