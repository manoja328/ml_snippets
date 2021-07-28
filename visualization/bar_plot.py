#difference in gcn and mlp
plt.figure(figsize=(12,4))
tick_marks = np.arange(len(class_names))
h = classwise_acc_gcn  - classwise_acc_mlp
plt.bar(range(len(classwise_acc)), h)
plt.ylim([-20,100])
plt.ylabel("Accuracy diff %")
plt.xticks(tick_marks, class_names, rotation=90)
plt.axvline(40,color='red')

for i, v in enumerate(h):
    if v<0:
        plt.text(i - 0.5, 40,  f"{v:.1f}", color='red',rotation=90)
    else:
        plt.text(i - 0.5, 40, f"{v:.1f}", color='blue', rotation=90)
plt.tight_layout()
plt.show()

print (np.array(class_names)[h<0])
asc = h.argsort() #sort the increase ascending
print ("most top 5 erronous class:")
print (np.array(class_names)[asc[:5]])
print (h[asc[:5]])
