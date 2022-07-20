import streamlit as st
import subprocess
from PIL import Image

st.header('🎈 R x Python Streamlit App')

st.sidebar.markdown('''
# About
This demo shows the use of R in a Streamlit App by showcasing 3 example use cases.

The R code for all 3 examples are rendered on-the-fly in this app.

R packages used:
- `ggplot2`
- `cowplot`
''')

st.subheader('1. Printing text in R')
with st.expander('See code'):
  code1 = '''print("Hello world ...")
  '''
  st.code(code1, language='R')
process1 = subprocess.Popen(["Rscript", "helloworld.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
st.write(result1)


st.subheader('2. Creating a plot using `ggplot2`')
with st.expander('See code'):
  code2 = '''library(ggplot2)

  ggplot(mtcars, aes(mpg, wt)) +
    geom_point()

  ggsave('plot.png')
  '''
  st.code(code2, language='R')
process2 = subprocess.Popen(["Rscript", "plot.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result2 = process2.communicate()
image = Image.open('plot.png')
st.image(image)
st.caption('**Figure 1.** A simple scatter plot of *wt* as a function of *mpg* from the mtcars dataset.')

st.subheader('3. Creating a plot of Lipinski descriptors using `ggplot2` and `cowplot`')
with st.expander('See code'):
  code3 = '''library(ggplot2)
  library(cowplot)
  data = read.csv("lipinski.csv", header = TRUE)
  d1 <- data.frame(a = c(1, 1,2, 2), b = c(720, 735, 735, 720))
  data$Activity <- factor(data$Activity, levels = c("Active", "Inactive"))
  p_1 <- ggplot(data, aes(factor(Activity), MW))
  p_1 <- p_1 + geom_boxplot(aes(fill = factor(Activity)), alpha = 0.7)
  p_1 <- p_1 + geom_hline(yintercept = 500, linetype="dashed", colour = "black")
  p_1 <- p_1 + ggtitle("MW") + theme_bw()
  p_1 <- p_1 + ylim(0,850) 
  p_1 <- p_1 + geom_line(data = d1, aes(x = a, y = b)) + annotate("text", x = 1.5, y = 750, label = "*", size = 8)
  p_1 <- p_1 + theme(plot.title = element_text(margin = margin (b = -22)),
                     panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                     aspect.ratio=1, legend.position = ("none"),
                     panel.border = element_rect(linetype = "solid",
                                                 colour = "black", fill = NA, size = 1),
                     axis.text.x = element_blank(),
                     axis.ticks.x = element_blank(),
                     axis.text.y = element_text(colour = "black", size = 15),
                     plot.margin = unit(c(0.25, 0.25, 0, 0.25), "cm"),
                     axis.title.y = element_blank(),
                     axis.title.x = element_blank())
  p_1 <- p_1 + theme(plot.title = element_text(size = 20, face = "bold", hjust = 0.5))

  p_2 <- ggplot(data, aes(factor(Activity), ALogP))
  d2 <- data.frame(a = c(1, 1,2, 2), b = c(6.8, 6.9, 6.9, 6.8))
  p_2 <- p_2 + geom_boxplot(aes(fill = factor(Activity)), alpha = 0.7)
  p_2 <- p_2 + geom_hline(yintercept = 5, linetype="dashed")
  p_2 <- p_2 + ggtitle("ALogP") + theme_bw()
  p_2 <- p_2 + ylim(0,8)
  p_2 <- p_2 + geom_line(data = d2, aes(x = a, y = b)) + annotate("text", x = 1.5, y = 7.1, label = "**", size = 8)
  p_2 <- p_2 + theme(plot.title = element_text(margin = margin (b = -22)),
                     panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                     aspect.ratio=1, legend.position = ("none"),
                     panel.border = element_rect(linetype = "solid",
                                                 colour = "black", fill = NA, size = 1),
                     axis.text.x = element_blank(),
                     axis.ticks.x = element_blank(),
                     axis.text.y = element_text(colour = "black", size = 15),
                     plot.margin = unit(c(0.25, 0.25, 0, 0), "cm"),
                     axis.title.y = element_blank(),
                     axis.title.x = element_blank())
  p_2 <- p_2 + theme(plot.title = element_text(size = 20, face = "bold", hjust = 0.5))

  p_3 <- ggplot(data, aes(factor(Activity), nHBDon))
  p_3 <- p_3 + geom_boxplot(aes(fill = factor(Activity)), alpha = 0.7)
  p_3 <- p_3 + geom_hline(yintercept = 5, linetype="dashed")
  p_3 <- p_3 + ggtitle("nHBDon") + theme_bw()
  p_3 <- p_3 + ylim(0,6.5)
  p_3 <- p_3 + theme(plot.title = element_text(margin = margin (b = -22)),
                     panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                     aspect.ratio=1, legend.position = ("none"),
                     panel.border = element_rect(linetype = "solid",
                                                 colour = "black", fill = NA, size = 1),
                     axis.text.x = element_text(colour = "black", size = 15),
                     axis.text.y = element_text(colour = "black", size = 15),
                     plot.margin = unit(c(0,0.25,0.25,0.25), "cm"),
                     axis.title.y = element_blank(),
                     axis.title.x = element_blank())
  p_3 <- p_3 + theme(plot.title = element_text(size = 20, face = "bold", hjust = 0.5))

  p_4 <- ggplot(data, aes(factor(Activity), nHBAcc))
  p_4 <- p_4 + geom_boxplot(aes(fill = factor(Activity)), alpha = 0.7)
  p_4 <- p_4 + geom_hline(yintercept = 10, linetype="dashed")
  p_4 <- p_4 + ggtitle("nHBAcc") + theme_bw()
  p_4 <- p_4 + ylim(0,12.5)
  p_4 <- p_4 + theme(plot.title = element_text(margin = margin (b = -22)),
                     panel.grid.major = element_blank(), panel.grid.minor = element_blank(),
                     aspect.ratio=1, legend.position = ("none"),
                     panel.border = element_rect(linetype = "solid",
                                                 colour = "black", fill = NA, size = 1),
                     axis.text.x = element_text(colour = "black", size = 15),
                     axis.text.y = element_text(colour = "black", size = 15),
                     plot.margin = unit(c(0,0.25,0.25, 0), "cm"),
                     axis.title.y = element_blank(),
                     axis.title.x = element_blank())
  p_4 <- p_4 + theme(plot.title = element_text(size = 20, face = "bold", hjust = 0.5))
  plot_grid(p_1, p_2, p_3, p_4, align = "hv")

  ggsave("lipinski.png", width = 8, height = 8)
  '''
  st.code(code3, language='R')
process3 = subprocess.Popen(["Rscript", "lipinski.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result3 = process3.communicate()
image = Image.open('lipinski.png')
st.image(image)
st.caption('**Figure 2.** A reproduction of Figure 3 from the [HCVpred](https://onlinelibrary.wiley.com/doi/abs/10.1002/jcc.26223) paper using code publicly available on [GitHub](https://github.com/chaninlab/hcvpred).')
