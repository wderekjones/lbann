import os, pytest

def test_checkpoint_lenet(exe, dirname):
    return_code_nockpt = os.system('salloc -N1 srun -n2 %s --model=%s/model_zoo/tests/model_lenet_mnist_ckpt.prototext --optimizer=%s/model_zoo/optimizers/opt_sgd.prototext --reader=%s/model_zoo/data_readers/data_reader_mnist.prototext --num_epochs=2' % (exe, dirname, dirname, dirname))
    
    os.system('patch -f  %s/model_zoo/tests/model_lenet_mnist_ckpt.prototext %s/model_zoo/tests/checkpoint_dir.patch' % (dirname, dirname))
    
    return_code_ckpt_1 = os.system('salloc -N1 srun -n2 %s --model=%s/model_zoo/tests/model_lenet_mnist_ckpt.prototext --optimizer=%s/model_zoo/optimizers/opt_sgd.prototext --reader=%s/model_zoo/data_readers/data_reader_mnist.prototext --num_epochs=1' % (exe, dirname, dirname, dirname))


    return_code_ckpt_2 = os.system('salloc -N1 srun -n2 %s --model=%s/model_zoo/tests/model_lenet_mnist_ckpt.prototext --optimizer=%s/model_zoo/optimizers/opt_sgd.prototext --reader=%s/model_zoo/data_readers/data_reader_mnist.prototext --num_epochs=2' % (exe, dirname, dirname, dirname))

    diff_test = os.system('diff ckpt/shared.epoch.2.step.1688 ckpt_none/shared.epoch.2.step.1688')
    os.system('rm -rf ckpt*')
    assert diff_test == 0
    













