#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:34:40 2018

@author: limalayla
"""

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm, mm
from math import ceil

margin = [2*cm, 3*cm]
question_size = [3.5*cm, 1*cm]
smallrect_size = [3*mm, 3*mm]
smallrect_margin = [1*mm, 1*mm]
mcqcounter = 0

def create_mcq(pdf, doctitle, nmcq):
    pagesize = A4
    orig = [margin[0], pagesize[1]-margin[1]]
    pdf = Canvas(filename, pagesize)
    pdf.setStrokeColorRGB(0, 0, 0)
    
    pdf.setFont('Courier-Bold', 20)
    draw_title(pdf, pagesize, doctitle)
    
    pos = [orig[0], orig[1]-3*cm]
    pdf.setFont('Courier', 9)
    
    nlines = ceil(nmcq / 20)
    for i in range(1, nlines+1):
        if (i%4==0):
            # New page
            pdf.showPage()
            pdf.setFont('Courier', 9)
            pos = list(orig)
        
        draw_line(pdf, pos)
        pos[1] -= 5.5*question_size[1] + 1*cm
    
    pdf.save()

def draw_title(pdf, size, title):
    pdf.drawCentredString(size[0]/2, size[1]-3*cm, doctitle)

def draw_line(pdf, pos):
    local_pos = list(pos)
    for i in range(4):
        draw_row(pdf, local_pos)
        local_pos[0] += question_size[0] + 1*cm

def draw_row(pdf, pos):
    local_pos = list(pos)
    
    pdf.rect(local_pos[0], local_pos[1], question_size[0], question_size[1]/2)

    label_pos = [pos[0]+question_size[0]-5*smallrect_size[0]-4*smallrect_margin[0]-1.5*mm,
                 pos[1]+question_size[1]/4-smallrect_size[1]/2+1]
    for i in range(5):
        pdf.drawString(label_pos[0], label_pos[1], chr(ord('A')+i))
        label_pos[0] += smallrect_size[0] + 1*mm
    
    local_pos[1] -= question_size[1]
    for i in range(5):
        draw_question(pdf, local_pos)
        local_pos[1] -= question_size[1]

def draw_question(pdf, pos):
    global mcqcounter
    mcqcounter += 1
    
    pdf.rect(pos[0], pos[1], question_size[0], question_size[1])
    pdf.drawString(pos[0] + 3*mm, pos[1] + question_size[1]/2-4, 'Q{}'.format(mcqcounter))
    
    smallrect_pos = [pos[0]+question_size[0]-5*smallrect_size[0]-4*smallrect_margin[0]-2*mm,
                     pos[1]+question_size[1]/2-smallrect_size[1]/2-1]
    
    for i in range(5):
        pdf.rect(smallrect_pos[0], smallrect_pos[1], smallrect_size[0], smallrect_size[1])
        smallrect_pos[0] += smallrect_size[0] + 1*mm

if __name__=='__main__':
    filename = 'example.pdf'
    doctitle = 'Example MCQ'
    nmcq = 200
    create_mcq(filename, doctitle, nmcq)
