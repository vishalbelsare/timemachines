from timemachines.skatertools.data.real import hospital
import random
from timemachines.skaters.sk.skinclusion import using_sktime
from timemachines.skaters.sk.sfinclusion import using_statsforecast
from timemachines.skating import prior

if using_sktime and using_statsforecast:
    from timemachines.skaters.sk.sfautoarimahypocratic import SF_HYPOCRATIC_SKATERS

    def test_random_skater(show=False):
        k = 3
        n = 100
        f = random.choice(SF_HYPOCRATIC_SKATERS)
        y = hospital(n=n)
        neg_y = [-yt for yt in y]
        e = [-1]*90+[100]+[-1]*90
        x, x_std = prior(f=f, y=neg_y, k=k, e=e )


if __name__ == '__main__':
    import time
    for _ in range(100):
        st = time.time()
        test_random_skater()
        print(time.time()-st)
