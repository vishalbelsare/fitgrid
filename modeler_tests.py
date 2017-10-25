# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from eegr import modeler as modl
import pdb
import logging 

# update these as more junk is added to the fit buckets
test_fields = ['time', 'chan', 'diagnostics']

def make_FitGrid(ntimes, nchans):
    ''' returns a fit grid for the tests to use '''

    times = [-1 * round((ntimes)/2) + t for t in range(ntimes)]
    chans = ['ch_{0}'.format(ch) for ch in range(nchans)]
    times_chans = modl.FitGrid(ntimes, nchans)
    for c,chan in enumerate(chans):
        for t,time in enumerate(times):
            times_chans[t,c].time = time
            times_chans[t,c].chan = chan
        
            # these are stubs ... set with actual values 
            times_chans[t,c].reg_fit['params'] =  ['b_0', 'b_1', 'b_2']
            times_chans[t,c].reg_fit['hat_matrix'] =  ['stub']
            times_chans[t,c].diagnostics['cooks_stuff'] = 'stub'
            times_chans[t,c].diagnostics['other_stuff'] = 'stub'

    return(times_chans)

def test_small_FitGrid(ntimes=17, nchans=4):
    times_chans = make_FitGrid(ntimes, nchans)

def test_large_FitGrid(ntimes=10000, nchans=128):
    ''' 10 seconds at 1000 samples/seconds x 128 channels '''
    times_chans = make_FitGrid(ntimes, nchans)

def test_get_bucket_at(ntimes=17,nchans=4):
    times_chans = make_FitGrid(ntimes, nchans)
    for time in range(ntimes):
        for chan in range(nchans):
            print(( 'bucket[{0},{1}]: time_idx {2}: {3}'
                    ', chan_jdx {4}: {5}' ).format(
                        time,chan,
                        times_chans[time,chan].time_idx, 
                        times_chans[time,chan].time,
                        times_chans[time,chan].chan_jdx,
                        times_chans[time,chan].chan,
                    ) )
            
def test_bucket_grid_getters(ntimes=17,nchans=4):
    b_grid = make_FitGrid(ntimes, nchans)
    for field in test_fields:
        got_em = getattr(b_grid, field)

def test_slicing_fail(ntimes=17, nchans=4):
    ''' check that FitGrid blocks slicing '''
    b_grid = make_FitGrid(ntimes, nchans)
    for field in test_fields:
        
        # try to access grid column slice
        try:
            got_em = getattr(b_grid[:,0], field)
        except:
            pass
            # print('caught column slicing error')
        else:
            msg = 'uh oh, failed to catch grid column slicing error'
            raise RuntimeError(msg)

        # try to access grid column slice
        try:
            got_em = getattr(b_grid[0,:], field)
        except:
            pass
            # print('caught column slicing error')
        else:
            msg = 'uh oh, failed to catch grid row slicing error'
            raise RuntimeError(msg)




