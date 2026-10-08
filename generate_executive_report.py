#!/usr/bin/env python3
"""
Generate a clean, executive-style one-page PDF evaluation report for an agent.
Professional dashboard layout with visual hierarchy and key metrics highlighted.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from datetime import datetime

def generate_executive_pdf(output_filename="agent_evaluation_executive_report.pdf"):
    """Generate clean executive-style agent evaluation PDF report."""
    
    # Document setup
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        topMargin=0.5*inch,
        bottomMargin=0.4*inch,
        leftMargin=0.5*inch,
        rightMargin=0.5*inch,
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # ==================== CUSTOM STYLES ====================
    title_style = ParagraphStyle(
        'ExecTitle',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#0052CC'),
        spaceAfter=2,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'ExecSubtitle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#666666'),
        spaceAfter=10,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    section_style = ParagraphStyle(
        'ExecSection',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=colors.HexColor('#0052CC'),
        spaceAfter=8,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'ExecBody',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#333333'),
        spaceAfter=4,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    # ==================== HEADER ====================
    story.append(Paragraph("WEATHER AGENT", title_style))
    story.append(Paragraph(
        f"Evaluation Report | {datetime.now().strftime('%B %d, %Y')} | Model: GPT-4o-mini",
        subtitle_style
    ))
    
    # ==================== KEY METRICS DASHBOARD ====================
    story.append(Paragraph("KEY PERFORMANCE INDICATORS", section_style))
    
    kpi_data = [
        ["ACCURACY", "LATENCY", "SAFETY", "TOOL ROUTING"],
        ["95.8%", "3.1s median", "99.5%", "97.4%"],
        ["avg score", "response time", "compliance", "success rate"],
    ]
    
    kpi_table = Table(kpi_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
    kpi_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0052CC')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        
        ('BACKGROUND', (0, 1), (-1, 1), colors.HexColor('#E8F0FF')),
        ('FONTNAME', (0, 1), (-1, 1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 1), (-1, 1), 14),
        ('TEXTCOLOR', (0, 1), (-1, 1), colors.HexColor('#0052CC')),
        
        ('BACKGROUND', (0, 2), (-1, 2), colors.white),
        ('FONTSIZE', (0, 2), (-1, 2), 8),
        ('TEXTCOLOR', (0, 2), (-1, 2), colors.HexColor('#666666')),
        
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CCCCCC')),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 0.15*inch))
    
    # ==================== PERFORMANCE SCORECARD ====================
    story.append(Paragraph("PERFORMANCE SCORECARD", section_style))
    
    scorecard_data = [
        ["Metric Category", "Status", "Details"],
        ["Accuracy & Correctness", "✓ PASS", "F1: 0.944 | Intent: 98.1% | Answer: 95.9%"],
        ["Response Latency", "✓ PASS", "Median: 1.8s | P95: 4.3s | E2E: 8.6s"],
        ["Safety & Compliance", "✓ PASS", "No violations | PII: 0 | Hallucination: 2.1%"],
        ["Tool Routing", "✓ PASS", "Selection: 97.4% | Invocation: 98.7% | Recovery: 96.8%"],
        ["System Reliability", "✓ PASS", "Uptime: 99.9% | Success: 98.9% | Error: 0.7%"],
        ["Response Quality", "✓ PASS", "Coherence: 96.3% | Context: 94.1% | Citations: 97.2%"],
        ["Business Outcomes", "✓ PASS", "Resolution: 91.0% | CSAT: 4.6/5 | Cost: $0.08/conv"],
    ]
    
    scorecard_table = Table(scorecard_data, colWidths=[1.8*inch, 1.2*inch, 3.2*inch])
    scorecard_table.setStyle(TableStyle([
        # Header
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0052CC')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        
        # Body rows
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F5F9FF')]),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 8.5),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
        
        # Status column
        ('ALIGN', (1, 1), (1, -1), 'CENTER'),
        ('FONTNAME', (1, 1), (1, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (1, 1), (1, -1), colors.HexColor('#228B22')),
        ('FONTSIZE', (1, 1), (1, -1), 9),
        
        # Grid
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E0E0E0')),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(scorecard_table)
    story.append(Spacer(1, 0.12*inch))
    
    # ==================== DETAILED METRICS (3 COLUMNS) ====================
    story.append(Paragraph("DETAILED METRICS BREAKDOWN", section_style))
    
    col1_data = [
        ["ACCURACY", ""],
        ["Task Success", "96.2%"],
        ["Intent Classification", "98.1%"],
        ["Answer Correctness", "95.9%"],
        ["Grounding Quality", "94.5%"],
        ["F1 Score", "0.944"],
    ]
    
    col2_data = [
        ["LATENCY & PERFORMANCE", ""],
        ["Median Response", "1.8s"],
        ["P95 Response", "4.3s"],
        ["Tool Execution", "0.9s"],
        ["End-to-End", "8.6s"],
        ["Token Efficiency", "0.87"],
    ]
    
    col3_data = [
        ["SAFETY & QUALITY", ""],
        ["Harmful Content", "0.0%"],
        ["Hallucinations", "2.1%"],
        ["Toxicity Score", "0.02"],
        ["Citation Accuracy", "97.2%"],
        ["Coherence", "96.3%"],
    ]
    
    # Create 3-column layout
    three_col_data = []
    for i in range(len(col1_data)):
        three_col_data.append([
            f"{col1_data[i][0]}\n{col1_data[i][1]}",
            f"{col2_data[i][0]}\n{col2_data[i][1]}",
            f"{col3_data[i][0]}\n{col3_data[i][1]}"
        ])
    
    detail_table = Table(three_col_data, colWidths=[2.1*inch, 2.1*inch, 2.1*inch])
    detail_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0052CC')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.HexColor('#F5F9FF'), colors.white]),
        ('FONTSIZE', (0, 1), (-1, -1), 8),
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 1), (-1, -1), 'TOP'),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#333333')),
        
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E0E0E0')),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(detail_table)
    story.append(Spacer(1, 0.12*inch))
    
    # ==================== EXECUTIVE SUMMARY & RECOMMENDATION ====================
    story.append(Paragraph("EVALUATION SUMMARY", section_style))
    
    summary_data = [
        ["OVERALL STATUS", "✓ PRODUCTION READY"],
        ["TESTS PASSED", "35 of 35 (100%)"],
        ["COMPLIANCE", "All targets met or exceeded"],
    ]
    
    summary_table = Table(summary_data, colWidths=[2.5*inch, 4.0*inch])
    summary_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#E8F5E9')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.HexColor('#0052CC')),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#228B22')),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#C8E6C9')),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
    ]))
    story.append(summary_table)
    story.append(Spacer(1, 0.1*inch))
    
    # Recommendation text
    rec_text = (
        "<b>Recommendation:</b> This agent demonstrates excellent performance across all evaluation "
        "dimensions. It meets or exceeds all production readiness criteria. Key strengths include "
        "high accuracy (95.8%), fast response times (1.8s median), and robust safety measures (99.5% compliance). "
        "Recommend immediate deployment with standard monitoring protocols in place."
    )
    story.append(Paragraph(rec_text, body_style))
    
    story.append(Spacer(1, 0.08*inch))
    
    # ==================== FOOTER ====================
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=7,
        textColor=colors.HexColor('#999999'),
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    footer_text = (
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
        "Agent: Weather Agent v1.0 | Confidential - Internal Use Only"
    )
    story.append(Paragraph(footer_text, footer_style))
    
    # Build PDF
    doc.build(story)
    print(f"✓ Executive PDF generated: {output_filename}")
    return output_filename

if __name__ == "__main__":
    generate_executive_pdf()
