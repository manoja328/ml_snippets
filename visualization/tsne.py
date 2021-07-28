data = []
y = []
for label in save:
    data.extend(save[label])
    y.extend([label] * len(save[label]))
data_np = np.concatenate(data)
y = np.array(y)

print(data_np.shape, y.shape)

# %%
from MulticoreTSNE import MulticoreTSNE
from matplotlib import pyplot as plt

embeddings = MulticoreTSNE(n_jobs=4, perplexity=50).fit_transform(data_np)

vis_x = embeddings[:, 0]
vis_y = embeddings[:, 1]
unique_c = np.unique(y)
Nclass = 20

plt.figure(figsize=(12, 8))
plt.scatter(vis_x, vis_y, c=y, cmap=plt.cm.get_cmap("tab20", Nclass), marker='.')
# plt.scatter(vis_x, vis_y, c=y, cmap=plt.cm.get_cmap("jet", Nclass), marker='.')
plt.colorbar(ticks=range(Nclass + 1))
plt.title("Multicore TSNE results for {} classes".format(Nclass))
plt.savefig("tsne.png", dpi=200)
plt.show()
