from tqdm import tqdm
# Defines number of epochs
n_epochs = 200

losses = []

for epoch in tqdm(range(n_epochs)):
    # inner loop
    loss = mini_batch(device, train_loader, train_step_fn)
    losses.append(loss)
