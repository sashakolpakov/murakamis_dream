# A proved left-contour comparison and the finite real seam

Research result, 7 November 2026. The two remaining derivative
inequalities have been certified on their entire prescribed compact
rectangle. Together with the direct endpoint estimate, this proves
the proposed left-contour phase comparison. The separately written
contour argument then bounds the original finite source at the real
outgoing endpoint, including its short half-grid continuation.

These are estimates for the specified Fourier boundary source. They
do not yet bound the entire outgoing vertical integral, assemble a
general attached source, or establish a new knot-family theorem.

## 1. The complete premise

Use exactly the notation and geometric output of
[the derivative reduction](research_mixed_fourier_left_taper_reduction.md).
For \(c=11/50\), \(0\le\lambda\le51/110\), put
\(q(t)=t-i\lambda t\). For the retained index
\(s=u+iv\), its containing domain is
\[
          1/8\le u\le1/2,\qquad 1/2\le e^{2\pi v}\le1.
\]
The phase derivative is
\[
 \frac{d}{dt}\Re\mathscr F_\eta(s,a,q(t))
   =\Re[(1-i\lambda)\{\Log(1-SQ)-\Log(1-Q)
                         -\Log(1-YQ)+\Log Y\}],
 \quad S=e^{-2\pi is},\ Q=e^{-2\pi iq(t)}.
 \tag{1}
\]
All logarithms have the determinations fixed in that reduction.
Its exact endpoint and radius minimization bounds (1) below by
\(\min(H_-,H_+)\). Its analytic Lemma 2 proves a lower bound
\(3/4\) for \(0<t\le1/100\).

The [fixed protocol](research_mixed_fourier_left_taper_protocol.md)
addresses the rest, \(1/100\le t\le11/50\). It covers the two
variables by 512 by 256 closed rectangles, retaining the full original
saved enclosure of \(Y\) in every cell. The sole execution passed
all 131072 cells. Every logarithm argument was enclosed in the right
half-plane before evaluation. The smallest saved lower endpoint for
either function is
\[
                   b_* =\frac{5917819973}{274877906944}>\frac1{50}.
 \tag{2}
\]
The rational comparison follows by multiplication:
\(50\cdot5917819973=295890998650>274877906944\).

| Artifact | SHA-256 |
|---|---|
| Derivative reduction | eb64296ffe3ad8849a3350f1155ca34d30bbc34003ff7a397a513e6b143d5801 |
| Fixed protocol | af9426ee67af62acc8cec618f8dd27c647e0b9fff958b87dc87c4573d9c936c3 |
| Frozen checker | 2f58b3f2a157e84e4a4f9082fd2407ac472c8de70ed0c6a63e44a6b5652c8f7e |
| Sole completed result | 55a7c56f33f576c9e6b13b015fd69a448c269ccda82166682675e06d76bcc4c9 |

The [saved result](../repro/results/research-mixed-fourier-left-taper.json)
contains every outward dyadic interval. All prescribed analytic counts
were completed, all 29 bindings remained unchanged, and there were no
inconclusive cells, refinements or retries. The
[review record](research_mixed_fourier_left_taper_review.md) distinguishes
the pre-execution proof and code reviews from the read-only inspection
of the output. No previously saved certificate was executed again.

Consequently, on the entire proposed taper,
\[
             \frac{d}{dt}\Re\mathscr F_\eta(s,a,q(t))>1/50.
 \tag{3}
\]
Integration gives
\[
 \Re\mathscr F_\eta(s,a,q(t))
 \le\Re\mathscr F_\eta(s,a,c-i\lambda c)-\frac{c-t}{50}.
 \tag{4}
\]
At \(t=0\), the continuous phase value exists. Keeping just the
stronger initial hundredth in the integral also gives the useful
fixed loss
\[
 \Re\mathscr F_\eta(s,a,0)
       <\Re\mathscr F_\eta(s,a,c-i\lambda c)-3/400.
 \tag{5}
\]
The incoming parameter and its allocation are unchanged throughout.

## 2. The finite source at the real endpoint

Use the actual correlated incoming family, supporting plane
\(B_\eta(x)\), original halfweight \(d_N(X)\), and finite
low source \(S_N^<(q)\) in
[the retained seam theorem](research_mixed_fourier_real_seam_contour.md).
In particular,
\[
 S_N^<(q)=\widehat f_N(q;y)
       \sum_{j=0}^{\lceil N/2\rceil-1}
           \frac{X^{-j}p_j(X)p_j(e^{-2\pi iq})}{P_j^3},
 \quad P_j=(r;r)_j,\ p_j(Z)=(rZ;r)_j,\ r=e^{-2\pi i/N}.
 \tag{6}
\]
The preceding certificate proves exactly premise (T) of that theorem.
It follows that, for all sufficiently large levels of either parity,
uniformly on its actual incoming family,
\[
 |d_N(X)|^{\eta/2}
    \sup_{-1/(2N)\le q\le0}|S_N^<(q)|
                  \le e^{N(B_\eta(x)-1/1000)}.
 \tag{7}
\]
This conclusion uses the complete retained contour: its main integral,
both discrete aliases, every vertical join, and the physical low tail.
The short real continuation in (7) uses the exact reciprocal factorial,
including its endpoint normalization. No central coherent sum is
replaced by the sum of its absolute terms.

At the physical endpoint \(q=0\), add the separately proved absolute
high-row estimate. With the complete conditional kernel
\(C_{1,N}\) and literal cardinal value \(f_0(y)\), this yields
\[
 |d_N(X)|^{\eta/2}|f_0(y)C_{1,N}(X,1)|
                  \le e^{N(B_\eta(x)-1/140000)}.
 \tag{8}
\]
All original factors remain present. In particular (8) is not an
estimate for a rescaled invariant obtained by dividing out a Fourier
weight.

## 3. What this does not settle

Equation (4) is a phase comparison along a complete left taper.
To turn every point of that taper into a uniform finite-source bound,
one must also control its retained aliases, physical low rows and the
reciprocal factorial near zero; the proof of (7) covers only the stated
short real segment. The central part of the outgoing vertical current
at nonzero height remains a separate coherent sum. Neighboring
attachment parameters also still have to be moved together.

Thus (7)--(8) remove a genuine endpoint obstruction. They do not prove
stability under arbitrary short partial fillings, which remains the
essential missing hypothesis for the finite-exception theorem.
