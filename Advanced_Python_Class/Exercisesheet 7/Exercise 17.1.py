import pearson as p

print(p.pearson_coefficient(p.generate_x_y_gaussians(5)[0], p.generate_x_y_gaussians(5)[1]))
print(p.pearson_coefficient(p.generate_x_y_gaussians(10)[0], p.generate_x_y_gaussians(10)[1]))
print(p.pearson_coefficient(p.generate_x_y_gaussians(50)[0], p.generate_x_y_gaussians(50)[1]))
print(p.pearson_coefficient(p.generate_x_y_gaussians(500)[0], p.generate_x_y_gaussians(500)[1]))