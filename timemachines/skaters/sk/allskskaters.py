from timemachines.skaters.sk.sktheta import SK_THETA_SKATERS
from timemachines.skaters.sk.skautoarima import SK_AA_SKATERS
from timemachines.skaters.sk.skautoets import SK_AE_SKATERS
from timemachines.skaters.sk.sfautoarima import SF_AA_SKATERS
from timemachines.skaters.sk.sfautoarimawiggly import SF_AUTOARIMA_WIGGLY_SKATERS
from timemachines.skaters.sk.skautoarimawiggly import SK_AUTOARIMA_WIGGLY_SKATERS
SK_SKATERS = SK_THETA_SKATERS + SK_AA_SKATERS + SK_AE_SKATERS +\
             SF_AA_SKATERS + SF_AUTOARIMA_WIGGLY_SKATERS + SK_AUTOARIMA_WIGGLY_SKATERS
