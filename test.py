import argparse
import torch
import torch.distributed as dist

parser = argparse.ArgumentParser()
parser.add_argument("--local_rank", type=int)
args = parser.parse_args()
device = args.local_rank

dist.init_process_group('nccl')

torch.cuda.set_device(device)

x = torch.rand([int(28e8), 2], device='cuda')
y = torch.rand([int(10e8), 2], device='cuda')
while True:
    #dist.all_reduce(y)
    #print(f"post all-reduce {x.numel()}")
    torch.cuda._sleep(10000)
print(x.shape, y.shape)

