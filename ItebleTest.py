print('_' not in 'test_ff')

fn = '201803契約台帳 (002)'
print(all((s not in fn) for s in ['_', 'コマツケア', 'KOSMIC', 'sell_used', '_20170726']))
print('_' not in fn)