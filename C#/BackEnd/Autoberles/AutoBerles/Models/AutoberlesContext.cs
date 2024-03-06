using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace AutoBerles.Models;

public partial class AutoberlesContext : DbContext
{
    public AutoberlesContext()
    {
    }

    public AutoberlesContext(DbContextOptions<AutoberlesContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Autok> Autoks { get; set; }

    public virtual DbSet<Berlok> Berloks { get; set; }

    public virtual DbSet<Kolcsonze> Kolcsonzes { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see http://go.microsoft.com/fwlink/?LinkId=723263.
        => optionsBuilder.UseMySQL("SERVER=localhost;PORT=3306;DATABASE=autoberles;USER=root;PASSWORD=;SSL MODE=none;");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Autok>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PRIMARY");

            entity.ToTable("autok");

            entity.Property(e => e.Id)
                .HasColumnType("int(11)")
                .HasColumnName("id");
            entity.Property(e => e.Evjarat)
                .HasColumnType("year(4)")
                .HasColumnName("evjarat");
            entity.Property(e => e.Rendszam)
                .HasMaxLength(6)
                .HasColumnName("rendszam");
            entity.Property(e => e.Szin)
                .HasMaxLength(30)
                .HasColumnName("szin");
            entity.Property(e => e.Tipus)
                .HasMaxLength(100)
                .HasColumnName("tipus");
        });

        modelBuilder.Entity<Berlok>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PRIMARY");

            entity.ToTable("berlok");

            entity.HasIndex(e => e.Jogositvanyszama, "jogositvanyszama").IsUnique();

            entity.HasIndex(e => e.Nev, "nev").IsUnique();

            entity.Property(e => e.Id)
                .HasColumnType("int(11)")
                .HasColumnName("id");
            entity.Property(e => e.Jogositvanyszama)
                .HasMaxLength(15)
                .HasColumnName("jogositvanyszama");
            entity.Property(e => e.Lakcim)
                .HasMaxLength(100)
                .HasColumnName("lakcim");
            entity.Property(e => e.Nev)
                .HasMaxLength(100)
                .HasColumnName("nev");
            entity.Property(e => e.Szuletesiido)
                .HasColumnType("date")
                .HasColumnName("szuletesiido");
            entity.Property(e => e.Telefonszam)
                .HasMaxLength(20)
                .HasColumnName("telefonszam");
        });

        modelBuilder.Entity<Kolcsonze>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PRIMARY");

            entity.ToTable("kolcsonzes");

            entity.HasIndex(e => e.Autoid, "autoid");

            entity.HasIndex(e => e.Berletkezdete, "berletkezdete").IsUnique();

            entity.HasIndex(e => e.Berloid, "berloid");

            entity.HasIndex(e => e.Napidij, "napidij").IsUnique();

            entity.Property(e => e.Id)
                .HasColumnType("int(11)")
                .HasColumnName("id");
            entity.Property(e => e.Autoid)
                .HasColumnType("int(11)")
                .HasColumnName("autoid");
            entity.Property(e => e.Berletkezdete)
                .HasColumnType("datetime")
                .HasColumnName("berletkezdete");
            entity.Property(e => e.Berloid)
                .HasColumnType("int(11)")
                .HasColumnName("berloid");
            entity.Property(e => e.Napidij).HasColumnName("napidij");
            entity.Property(e => e.Napokszama)
                .HasColumnType("int(11)")
                .HasColumnName("napokszama");

            entity.HasOne(d => d.Berlo).WithMany(p => p.Kolcsonzes)
                .HasForeignKey(d => d.Berloid)
                .HasConstraintName("kolcsonzes_ibfk_2");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
