using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace monthypython.Models;

public partial class MonthypythonContext : DbContext
{
    public MonthypythonContext()
    {
    }

    public MonthypythonContext(DbContextOptions<MonthypythonContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Epizodok> Epizodoks { get; set; }

    public virtual DbSet<Forgatokonyv> Forgatokonyvs { get; set; }

    public virtual DbSet<Tipusok> Tipusoks { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see http://go.microsoft.com/fwlink/?LinkId=723263.
        => optionsBuilder.UseMySQL("SERVER=localhost;PORT=3306;DATABASE=monthypython;USER=root;PASSWORD=;SSL MODE=none;");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Epizodok>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PRIMARY");

            entity.ToTable("epizodok");

            entity.Property(e => e.Id)
                .HasColumnType("int(11)")
                .HasColumnName("id");
            entity.Property(e => e.Nev)
                .HasMaxLength(30)
                .HasColumnName("nev");
            entity.Property(e => e.Sorozat)
                .HasMaxLength(10)
                .HasColumnName("sorozat");
        });

        modelBuilder.Entity<Forgatokonyv>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PRIMARY");

            entity.ToTable("forgatokonyv");

            entity.HasIndex(e => e.Epizodid, "epizodid");

            entity.HasIndex(e => e.Tipusid, "tipusid");

            entity.Property(e => e.Id)
                .HasColumnType("int(11)")
                .HasColumnName("id");
            entity.Property(e => e.Epizodid)
                .HasColumnType("int(11)")
                .HasColumnName("epizodid");
            entity.Property(e => e.FelvetelDatuma)
                .HasColumnType("date")
                .HasColumnName("felvetel_datuma");
            entity.Property(e => e.Karakter)
                .HasMaxLength(30)
                .HasColumnName("karakter");
            entity.Property(e => e.LejatszasDatuma)
                .HasColumnType("date")
                .HasColumnName("lejatszas_datuma");
            entity.Property(e => e.Resz)
                .HasMaxLength(30)
                .HasColumnName("resz");
            entity.Property(e => e.Reszletek)
                .HasColumnType("text")
                .HasColumnName("reszletek");
            entity.Property(e => e.Szinesz)
                .HasMaxLength(30)
                .HasColumnName("szinesz");
            entity.Property(e => e.Tipusid)
                .HasColumnType("int(11)")
                .HasColumnName("tipusid");

            entity.HasOne(d => d.Epizod).WithMany(p => p.Forgatokonyvs)
                .HasForeignKey(d => d.Epizodid)
                .HasConstraintName("forgatokonyv_ibfk_2");

            entity.HasOne(d => d.Tipus).WithMany(p => p.Forgatokonyvs)
                .HasForeignKey(d => d.Tipusid)
                .HasConstraintName("forgatokonyv_ibfk_1");
        });

        modelBuilder.Entity<Tipusok>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("PRIMARY");

            entity.ToTable("tipusok");

            entity.Property(e => e.Id)
                .HasColumnType("int(11)")
                .HasColumnName("id");
            entity.Property(e => e.Tipus)
                .HasMaxLength(30)
                .HasColumnName("tipus");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
