import matplotlib.pyplot as plt
from rectpack import newPacker

# إعداد البيانات
bin_width = 100  # عرض اللوح (سم)
bin_height = 100  # ارتفاع اللوح (سم)

# إنشاء كائن التعبئة
packer = newPacker(rotation=True)  # السماح بتدوير القطع لتحسين التعبئة

# إضافة القطع المطلوبة
for _ in range(10):
    packer.add_rect(25, 25)

for _ in range(5):
    packer.add_rect(40, 40)

# إضافة الألواح المتاحة
packer.add_bin(bin_width, bin_height)

# تنفيذ التعبئة
packer.pack()

# رسم النتائج مع المسطرة
def draw_packing_with_rulers(packer):
    """ترسم الألواح مع القطع المعبأة عليها وتضيف مسطرة أفقية وعمودية."""
    num_bins = len(packer)  # عدد الألواح المستخدمة
    fig, axes = plt.subplots(1, num_bins, figsize=(6 * num_bins, 6))
    
    # إذا كان لدينا لوح واحد فقط، نضعه في قائمة ليسهل التعامل معه
    if num_bins == 1:
        axes = [axes]
    
    for i, bin in enumerate(packer):
        ax = axes[i]
        ax.set_xlim(0, bin_width)
        ax.set_ylim(0, bin_height)
        ax.set_title(f"لوح رقم {i + 1}")
        ax.set_xlabel("العرض (سم)")
        ax.set_ylabel("الارتفاع (سم)")
        ax.set_aspect('equal')
        
        # إضافة خطوط الشبكة (المسطرة)
        ax.set_xticks(range(0, bin_width + 1, 10))  # كل 10 سم
        ax.set_yticks(range(0, bin_height + 1, 10))  # كل 10 سم
        ax.grid(which='both', color='gray', linestyle='--', linewidth=0.5)

        # رسم كل قطعة داخل اللوح
        for rect in bin:
            x, y, w, h = rect.x, rect.y, rect.width, rect.height
            ax.add_patch(plt.Rectangle((x, y), w, h, edgecolor="black", facecolor="lightblue"))
            ax.text(x + w / 2, y + h / 2, f"{w}x{h}", color="black", ha="center", va="center")
        
        # رسم إطار اللوح
        ax.add_patch(plt.Rectangle((0, 0), bin_width, bin_height, edgecolor="red", fill=False, linewidth=2))
    
    plt.tight_layout()
    plt.show()

# استدعاء الدالة لرسم النتائج مع المسطرة
draw_packing_with_rulers(packer)
