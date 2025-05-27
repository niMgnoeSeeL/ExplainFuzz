"builtin.module"() ({
  "func.func"() <{function_type = (f80) -> f80, sym_name = "arith_negf_f80"}> ({
  ^bb0(%arg0: f80):
    %0 = "arith.negf"(%arg0) <{fastmath = #arith.fastmath<none>}> : (f80) -> f80
    "func.return"(%0) : (f80) -> ()
  }) : () -> ()
}) : () -> ()

