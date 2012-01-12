import sys
import random

learning_rate = .2
num_features = None
train_lines = []
test_lines = []

def main(trainfile_string, testfile_string):
    global train_lines
    global test_lines
    global num_features
    train_lines = open(trainfile_string, 'r').readlines()
    test_lines = open(testfile_string, 'r').readlines()    
    num_features = len(train_lines[0].strip().split(',')) - 1
    
    # make a pass through the data once for each number other than 8
    # and classify n vs 8
    for n in xrange(10):
        if n != 8:
            test(n, getWeights(n))

            
def getWeights(num):
    "Train perceptron to differentiate between num and 8, \
    and return the trained weights weights"
    global learning_rate
    global num_features
    global train_lines
    # start with random weights in range (-1, 1)
    weights = [random.uniform(-1,1) for i in xrange(num_features)]
    for line in train_lines:
        # store a line of data as a list of ints
        data = [int(x) for x in line.strip().split(',')]
        # expected value must be -1 or 1
        if data[-1] == 8:
            t = 1
        elif data[-1] == num:
            t = -1
        else:
            continue
        
        # obtain o
        total = 0.0
        for i in xrange(num_features):
            total += weights[i]*data[i]
        o = sgn(total)

        # adjust the weights
        for i in xrange(num_features):
            weights[i] += learning_rate*(t - o)*data[i]
            
    return weights
    
def test(num, weights):
    global test_lines
    p = 0;
    n = 0;
    for line in test_lines:
        # store a line of data as a list of ints
        data = [int(x) for x in line.strip().split(',')]
        # expected value must be -1 or 1
        if data[-1] == 8:
            t = 1
        elif data[-1] == num:
            t = -1
        else:
            continue
        
        # obtain o
        total = 0.0
        for i in xrange(num_features):
            total += weights[i]*data[i]
        o = sgn(total)

        if (o == t):
            p = p + 1
        else:
            n = n + 1
    print('Success Rate = %f\n' % (float(p)/float(n + p)))
    
def sgn(val):
    if val > 0:
        return 1
    else:
        return -1

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'to train, please provide two filename arguments\n'
        sys.exit(1)
    else:
        main(sys.argv[1], sys.argv[2])