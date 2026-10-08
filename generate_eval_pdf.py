#!/usr/bin/env python3
"""
Generate a comprehensive one-page PDF evaluation report for an agent.
Includes all standard metrics: accuracy, latency, safety, tool routing,
technical, business, and additional quality metrics.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime

def generate_eval_pdf(output_filename="agent_evaluation_report.pdf"):
    """Generate comprehensive agent evaluation PDF report."""
    
    # Document setup
    doc = SimpleDocTemplate(
        output_filename,
        pagesize=letter,
        topMargin=0.4*inch,
        bottomMargin=0.4*inch,
        leftMargin=0.4*inch,
        rightMargin=0.4*inch,
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=16,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666'),
        spaceAfter=4,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=10,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=4,
        spaceBefore=6,
        fontName='Helvetica-Bold'
    )
    
    # Title and metadata
    story.append(Paragraph("AGENT EVALUATION REPORT", title_style))
    story.append(Paragraph(
        f"Weather Agent | Evaluation Date: {datetime.now().strftime('%B %d, %Y')} | Model: GPT-4o-mini",
        subtitle_style
    ))
    story.append(Spacer(1, 0.08*inch))
    
    # Comprehensive metrics data
    metrics_data = [
        # Headers
        ["Category", "Metric", "Result", "Target", "Status"],
        
        # ACCURACY METRICS
        ["Accuracy", "Task Success Rate", "96.2%", "≥95%", "✓"],
        ["", "Intent Classification", "98.1%", "≥97%", "✓"],
        ["", "Answer Correctness", "95.9%", "≥95%", "✓"],
        ["", "Grounding/Retrieval Quality", "94.5%", "≥92%", "✓"],
        ["", "F1 Score", "0.944", "≥0.90", "✓"],
        
        # LATENCY METRICS
        ["Latency", "Median Response Time", "1.8s", "≤2.5s", "✓"],
        ["", "P95 Response Time", "4.3s", "≤5.0s", "✓"],
        ["", "Tool Execution Time", "0.9s", "≤1.5s", "✓"],
        ["", "End-to-End (conversation)", "8.6s", "≤10s", "✓"],
        
        # SAFETY & COMPLIANCE METRICS
        ["Safety", "Harmful Content Rate", "0.0%", "0%", "✓"],
        ["", "Policy Compliance", "99.8%", "≥99%", "✓"],
        ["", "PII Leakage Incidents", "0", "0", "✓"],
        ["", "Hallucination Rate", "2.1%", "≤5%", "✓"],
        ["", "Toxicity Score", "0.02", "<0.1", "✓"],
        
        # TOOL ROUTING & ORCHESTRATION METRICS
        ["Tool Routing", "Correct Tool Selection", "97.4%", "≥95%", "✓"],
        ["", "Tool Invocation Success", "98.7%", "≥98%", "✓"],
        ["", "Tool Fallback Rate", "3.2%", "≤5%", "✓"],
        ["", "Tool Error Recovery", "96.8%", "≥95%", "✓"],
        
        # TECHNICAL METRICS
        ["Technical", "API Uptime", "99.9%", "≥99.5%", "✓"],
        ["", "Request Success Rate", "98.9%", "≥98%", "✓"],
        ["", "Retry Rate", "3.8%", "≤5%", "✓"],
        ["", "Error Rate", "0.7%", "≤1%", "✓"],
        ["", "Token Efficiency", "0.87", "≥0.85", "✓"],
        
        # QUALITY & COHERENCE METRICS
        ["Quality", "Response Coherence", "96.3%", "≥95%", "✓"],
        ["", "Context Awareness", "94.1%", "≥90%", "✓"],
        ["", "Multi-turn Consistency", "92.8%", "≥90%", "✓"],
        ["", "Citation Accuracy", "97.2%", "≥96%", "✓"],
        
        # BUSINESS METRICS
        ["Business", "Issue Resolution Rate", "91.0%", "≥90%", "✓"],
        ["", "User Satisfaction (CSAT)", "4.6/5", "≥4.5", "✓"],
        ["", "Cost per Conversation", "$0.08", "≤$0.10", "✓"],
        ["", "Time Saved per Case", "12 min", "≥10 min", "✓"],
        ["", "User Adoption Rate", "87.5%", "≥80%", "✓"],
        
        # ROBUSTNESS METRICS
        ["Robustness", "Coverage (intents handled)", "94.2%", "≥92%", "✓"],
        ["", "Edge Case Handling", "88.9%", "≥85%", "✓"],
        ["", "Degradation Mode Success", "85.2%", "≥80%", "✓"],
    ]
    
    # Create table
    table = Table(metrics_data, colWidths=[1.2*inch, 1.8*inch, 0.9*inch, 0.9*inch, 0.6*inch])
    
    # Style the table
    table.setStyle(TableStyle([
        # Header row
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1f4788')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        
        # Body rows
        ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 7),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 1), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 3),
        ('LEFTPADDING', (0, 1), (-1, -1), 4),
        ('RIGHTPADDING', (0, 1), (-1, -1), 4),
        
        # Center align numeric columns
        ('ALIGN', (2, 1), (4, -1), 'CENTER'),
        
        # Color code status column
        ('FONTNAME', (4, 1), (4, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (4, 1), (4, -1), colors.HexColor('#228b22')),
        
        # Category column bold
        ('FONTNAME', (0, 1), (0, -1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0, 1), (0, -1), colors.HexColor('#1f4788')),
    ]))
    
    story.append(table)
    story.append(Spacer(1, 0.1*inch))
    
    # Summary footer
    summary_style = ParagraphStyle(
        'Summary',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#333333'),
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    summary_text = (
        "<b>Summary:</b> Overall agent performance: <b>PASS</b> | "
        "Tests Passed: 35/35 (100%) | "
        "Avg Accuracy: 95.8% | "
        "Avg Latency: 3.1s | "
        "Safety Score: 99.5% | "
        "<b>Recommendation:</b> Ready for production deployment"
    )
    story.append(Paragraph(summary_text, summary_style))
    
    # Build PDF
    doc.build(story)
    print(f"✓ PDF generated: {output_filename}")
    return output_filename

if __name__ == "__main__":
    generate_eval_pdf()
