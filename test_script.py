import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import date
from glob import glob
files = glob(r'.\Tickets\*.xlsx')
print(files)
data = pd.read_excel(files[0])
node_down_tickets = data[data['Short description'].str.contains("Node_Down") == True].copy()
node_down_tickets['Touched By'] = np.where(node_down_tickets['Work notes'].str.contains("Merge Service Check") == True, "Automation","NOC")
automation_touched = node_down_tickets[node_down_tickets['Touched By'] == "Automation"].copy()
automation_touched['Resolved'] = np.where(automation_touched['Resolved by'] == "Okapi User", "Automation Resolved","NOC Resolved")
fig, axs = plt.subplots(1,2, figsize=(10,5))
sns.countplot(data=node_down_tickets, x='Touched By', hue='Touched By', ax=axs[0])
axs[0].set_title("Automation Touched "+str(date.today()))
sns.countplot(data=automation_touched, x='Resolved', hue='Resolved', ax=axs[1])
axs[1].set_title("Resolution Status "+str(date.today()))
plt.savefig("image.png")
