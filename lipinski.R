library(ggplot2)
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
