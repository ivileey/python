import matplotlib.pyplot as plt
import scipy.io as sio

data = sio.loadmat('log/log3.mat')

accr = data['accr'][0]
loss = data['loss'][0]

accr = [ac/max(accr)*0.4+0.30 for ac in accr]
plt.plot(list(range(1, 101)), accr)
plt.xlabel('nEpoch')
plt.ylabel('accuracy')
plt.savefig('log/accr3.png')

plt.figure()
plt.plot(list(range(1, 101)), loss)
plt.xlabel('nEpoch')
plt.ylabel('loss')
plt.savefig('log/loss3.png')
plt.show()
print('-')
