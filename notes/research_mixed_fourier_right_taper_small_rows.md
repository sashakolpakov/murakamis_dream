# Small retained indices and assembly on the incoming right taper

Research deduction, 7 November 2026. The physical retained rows below
the central cutoff have a uniform upper bound throughout the enlarged
incoming right taper. Their rates increase with the retained index
until that cutoff. The cutoff itself is bounded by the original
real-cut comparison and incoming transport. The outgoing comparisons
then cover the whole bent horizontal contour, including its true
half-grid endpoint.

This argument concerns the original small physical rows. Their
outgoing vertical current and right return are included in Section 4,
giving a bound for their complete finite outgoing sum. The central
physical sum is not estimated by absolute values here.
No numerical evaluation is used.

## 1. Parameters and exact rows

Retain the correlated reference and notation of
[incoming height transport](research_mixed_fourier_incoming_height_transport.md).
Write
\[
\begin{gathered}
 \eta\in\{0,1\},\qquad c=\Im a_*\in[-.108,0],\qquad
 h_q=\Im q_*\in[-.102,-.001],\\
 b=9/20,\qquad a=x+ih,\qquad b\le x\le1/2,\quad c\le h\le0,\\
 y=x_0,\quad Y=e^{2\pi iy},\qquad
 r=e^{-2\pi i/N},\quad X=e^{-2\pi ia},\\
 P_j=(r;r)_j,\qquad p_j(Z)=(rZ;r)_j,\qquad
 L_N=\lceil N/8\rceil,\quad
 \alpha_N=-1/(2N),\quad\beta_N=1+\alpha_N.
\end{gathered}
\tag{1}
\]
The original output satisfies \(|Y|<5/8\) and the bounds used in
[the right outgoing comparison](research_mixed_fourier_right_cap_upper_main_arc.md).
The finite row at outgoing parameter \(q\) is
\[
 T_{j,N}(q;a,y)
   =\frac{X^{-j}p_j(X)p_j(e^{-2\pi iq})}{P_j^3}
                         \widehat f_N(q;y),\qquad 0\le j<L_N,
\tag{2}
\]
where \(\widehat f_N\) is the original factorial cardinal, including
its factor \(1/N\). The absolute incoming multiplier remains
\(|d_N(X)|^{\eta/2}\).

Let \(M_\eta\), \(p_\eta\), and \(a_R=\Re a_*\) be the original
reference action, real incoming derivative, and real incoming
coordinate. Put
\[
 B_\eta(b)=M_\eta+p_\eta(b-a_R)-\kappa(b-a_R)^2,
 \qquad \kappa=1/2500000,
 \qquad
 B^{\rm small}_\eta(x,h)=B_\eta(b)-\frac\pi{10}(h-c).
\tag{3}
\]
In particular the reference plane stays at \(b\).

For \(0\le u\le1/8\), use the continuous physical-row rate
\[
 E_\eta(u;a,q)=\Re\{g(u+a)-g(a)+g(u+q)-g(q)-3g(u)
                  +2\pi iau+\ell_q(y)\}
                         -\frac\eta2\Re g(a).
\tag{4}
\]
All primitives retain their original branches. At \(u=0\) and
\(q=0\), use their continuous values. When \(\Im q<0\), the two
outgoing factorial primitives use the lower-half-plane continuation,
also beyond real part one. Formula (4) is the same row rate as in
[the original horizontal completion](research_mixed_fourier_right_horizontal_completion.md),
equation (4).

## 2. Increasing rates on the small-index interval

First let \(q=z+ih_q\), \(11/50\le z\le9/20\).
Set \(R_a=e^{2\pi h}\le1\) and \(R_q=e^{2\pi h_q}<1\).
For \(0<u\le1/8\), direct differentiation of (4) gives
\[
 \partial_u E_\eta
 =\log\frac{|R_a^{-1}-e^{-2\pi i(x+u)}|
                     |1-R_qe^{-2\pi i(z+u)}|}
                    {(2\sin\pi u)^3}.
\tag{5}
\]
The chirp in (4) is needed for the factor \(R_a^{-1}\).
Since \(.45\le x+u\le.625\), the cosine of its argument is
nonpositive, and the first modulus in (5) is at least one.
Also \(.22\le z+u\le.575\). If its cosine is nonpositive,
the second modulus is at least one. Otherwise \(z+u\in[.22,.25]\),
and minimizing over a nonnegative radius bounds that modulus below
by \(\sin(2\pi(z+u))\ge\sin(.44\pi)>9/10\).
For the last numerical inequality, write
\(\sin(.44\pi)=\cos(.06\pi)\) and use
\(.06\pi<1/5\) and \(\cos t\ge1-t^2/2\).
Finally \(\sin(\pi/8)<2/5\), as follows from
\(\sqrt2>34/25\) and its half-angle formula. Hence
\[
                 \partial_u E_\eta>\log(225/128)>0.
\tag{6}
\]
This is uniform on the stated incoming rectangle.

At the real cutoff \(u=1/8\), the
[all-height incoming transport](research_mixed_fourier_incoming_taper_all_height.md),
Lemma 2, first moves \(b+ic\) to \(x+ic\) without increasing
the rate. Equation (22) of the incoming-height note then lowers
it by at least \(\pi(h-c)/10\) when the height is raised.
The completed original real-cut inequality therefore gives
\[
 E_\eta(1/8;a,z+ih_q)
 <B^{\rm small}_\eta(x,h)
      -\kappa(z-\Re q_*)^2-1/35000 .
\tag{7}
\]
Integrating (6), and using continuity at zero, proves (7) with
the same right side for every \(0\le u\le1/8\).

For the outgoing left taper, put
\(q(t)=t-i\lambda t\), \(0\le t\le11/50\),
\(\lambda=-h_q/(11/50)\le51/110\).
At \(q=0\), the same derivative calculation gives
\[
 \partial_u E_\eta(u;a,0)
 =\log\frac{|R_a^{-1}-e^{-2\pi i(x+u)}|}
                    {(2\sin\pi u)^2}
 >\log(25/16)>0.
\tag{8}
\]
The difference between the derivatives at \(q(t)\) and at zero is
\[
 \log\frac{|1-e^{-2\pi\lambda t}e^{-2\pi i(u+t)}|}
                   {|1-e^{-2\pi iu}|}\ge0.
\tag{9}
\]
This is exactly the radius-angle inequality (13)--(14) in
[the left-taper completion](research_mixed_fourier_left_taper_source_completion.md);
its proof involves only \(u,t,\lambda\), so the new incoming
coordinate does not change it. The rates again increase to the
cutoff. At that cutoff the outgoing taper comparison is also
independent of \(a\), and bounds the rate by its value at
\(11/50+ih_q\). Equation (7) therefore yields
\[
 E_\eta(u;a,q(t))<B^{\rm small}_\eta(x,h)-1/35000.
\tag{10}
\]
At \(t=0\), the existing first-hundredth estimate gives the
additional decrease \(3/400\), although it is not needed below.

For the outgoing right interval, the original comparisons are
\[
\begin{split}
 \partial_z E_\eta(u;a,z+ih_q)&<-1/10
                                   &&(9/20\le z\le3/4),\\
 E_\eta(u;a,z+ih_q)&<E_\eta(u;a,z-1/2+ih_q)-1/200
                                   &&(3/4\le z\le1).
\end{split}
\tag{11}
\]
Their proofs use only \(0\le u\le1/2\), the nonpositive retained
height, and the original output. The incoming terms cancel from
both comparisons. Starting with (7) at \(z=9/20\), then applying
the second comparison to its targets in \([1/4,1/2]\), proves
\[
 E_\eta(u;a,z+ih_q)<B^{\rm small}_\eta(x,h)-1/35000
               \quad(9/20\le z\le1,\ 0\le u\le1/8).
\tag{12}
\]
This includes \(u=0\), where the incident factorial difference
vanishes and the cardinal alone supplies the rightward decrease.

## 3. The finite source and the true endpoint

Let \(\mathcal C_N\) be the oriented bent outgoing path consisting
of the real segment \([\alpha_N,0]\), the segment
\(q(t)=t-i\lambda t\) just used, and the horizontal segment
\([11/50,\beta_N]+ih_q\).

**Theorem 1.** Uniformly for the references and targets (1), at
all sufficiently large levels of either parity,
\[
 |d_N(X)|^{\eta/2}N\int_{\mathcal C_N}
             \sum_{j=0}^{L_N-1}|T_{j,N}(q;a,y)|\,|dq|
 \le \exp N\{B^{\rm small}_\eta(x,h)-1/70000\}.
\tag{13}
\]

*Proof.* The exact finite product bounds give rate (4), with
uniform polynomial factors and an arbitrarily small fixed rate
tolerance for the original incoming weight. These are the same
product bounds used in the left-taper and original horizontal
completion proofs. Their domains remain valid: the incoming
arguments have real parts in \([.45,.625]\), the negative-height
outgoing arguments use their global lower-half-plane continuation,
and the taper endpoint keeps its zero-safe product estimate.
The real physical factorial bound is uniform down to \(j=0\).
Also \((L_N-1)/N<1/8\), so (7), (10) and (12) cover all the
displayed rows without increasing their support.

The short real segment needs no new interpolation estimate in
the retained index. For \(\alpha_N\le q\le0\), \(1\le k\le j<L_N\),
one has
\[
 0<q+k/N\le k/N<1/8,
 \qquad |1-e^{-2\pi i(q+k/N)}|
                        \le|1-e^{-2\pi ik/N}|.
\tag{14}
\]
Consequently \(|p_j(e^{-2\pi iq})|\le|P_j|\), including the
empty product. The exact cardinal has
\(|\widehat f_N(q;y)|\le C|f_0(y)|\) on that segment, as proved
in Section 5 of
[the real-seam theorem](research_mixed_fourier_real_seam_contour.md).
Its relevant factorial arguments stay in the same fixed zero-free
neighborhoods; it does not depend on the new incoming parameter.
Thus each absolute row on this segment is at most a constant times
its own seam value. Estimate (10) applies to those seam values.

The path lengths are bounded, the number of rows is less than
\(N\), and the original outgoing factor is \(N\). Choose the
finite-rate tolerance below half of \(1/35000\), and absorb the
remaining fixed polynomial by the unused part of that gap. This
gives (13). No central-row cancellation is used. \(\square\)

If \(P_\eta\) is the original complex incoming derivative and
\(\mathcal L_\eta(a)=\Re\{\Pi_\eta^{\rm F}(a_*;x_0)
                                      +P_\eta(a-a_*)\}\), then
\[
 B^{\rm small}_\eta(x,h)-\mathcal L_\eta(x+ih)
 =-\Re P_\eta(x-b)+\{\Im P_\eta-\pi/10\}(h-c)
                         -\kappa(b-a_R)^2.
\tag{15}
\]
Its sign is not assigned here. The neighboring factor and the
original compensation still have to be included.

## 4. Vertical current, right return and complete finite sum

Define the exact small-row sources
\[
 S_N^{\rm small}(q)=\sum_{j=0}^{L_N-1}T_{j,N}(q;a,y),
 \qquad
 V_N^{\rm small}(a)=\sum_{l=0}^{N-1}
      \sum_{j=0}^{L_N-1}
       \frac{X^{-j}p_j(X)p_j(r^l)}{P_j^3}f_l(y).
\tag{16}
\]
The outgoing regrouping is valid separately for every retained
physical row, so it restricts to (16). In its notation,
\(w_{N,0}(v)=(1+e^{2\pi Nv})^{-1}-\mathbf1_{\{v<0\}}\),
and the full path is \(\mathcal C_N\) followed by the vertical
return from \(\beta_N+ih_q\) to \(\beta_N\). Thus
\[
\begin{split}
 V_N^{\rm small}
 ={}&N\int_{\mathcal C_N}S_N^{\rm small}(q)\,dq
      +N\int_{\beta_N+ih_q}^{\beta_N}S_N^{\rm small}(q)\,dq\\
 &+iN\int_{\mathbb R}w_{N,0}(v)
       \{S_N^{\rm small}(\beta_N+iv)
                        -S_N^{\rm small}(\alpha_N+iv)\}\,dv.
\end{split}
\tag{17}
\]
All three terms retain their original coefficients and cardinal
values.

The real-seam estimate proved in Section 2 is stronger than (10):
\[
 E_\eta(u;a,0)
 <B^{\rm small}_\eta(x,h)-3/400-1/35000,
                             \qquad 0\le u\le1/8.
\tag{18}
\]
Apply the physical-row vertical envelope, equation (19) of
[the real-endpoint theorem](research_mixed_fourier_real_endpoint_vertical_envelope.md),
to this subset of retained rows. Its proof extends unchanged to
the incoming targets (1): its outgoing rates \(P(u,v)\), \(K(v)\)
and \(L(u,v)\), including the right-cardinal decrement, are
independent of \(a\). The incoming product enters only through
the seam rate (18). Its uniform finite upper bound is valid on
the enlarged compact incoming set, and the actual incoming
halfweight still has upper rate \(-\eta\Re g(a)/2\).

This is also a uniform statement on the noncompact vertical ends.
The original explicit outgoing factorial remainders and the
disk-series corrections in equations (16a)--(17) of that theorem
are independent of \(a\). They tend uniformly to zero as the
chosen fixed height increases. The incoming factors remain the
same finite products. Here \(j<L_N\) even gives
\(N-2j>3N/4\) in the upper damping; the lower end has its
original damping proportional to \(N|v|\). Consequently (18)
and the unchanged row envelope prove, after one fixed tolerance
and polynomial absorption,
\[
\begin{split}
 &|d_N(X)|^{\eta/2}N\int_{\mathbb R}|w_{N,0}(v)|
       \sum_{j=0}^{L_N-1}
       \{|T_{j,N}(\beta_N+iv)|+|T_{j,N}(\alpha_N+iv)|\}\,dv\\
 &\hspace{25mm}\le
               e^{N\{B^{\rm small}_\eta(x,h)-1/1000\}}.
\end{split}
\tag{19}
\]
The finite cardinal estimate used here includes its possible
zero line; it never divides by that cardinal.

The unweighted return has its own comparison. For \(h_q\le v\le0\),
the negative-height physical-row inequality
\(L(u,v)\le L(u,0)+(\pi-\phi)v\), with \(\phi=2\pi\Re y\),
gives, after restoring the outgoing weight and including the
right cardinal, an upper change from the seam rate of
\[
                    (\pi+\phi)|v|-2\pi\Im y<-1/50.
\tag{20}
\]
This is equation (26) and the following comparison in
[the vertical-current completion](research_mixed_fourier_right_cap_vertical_current_completion.md).
Both its profile difference and its strict constant are independent
of the incoming parameter. The finite proof again uses polynomial
periodicity and the two distinct cardinal upper envelopes.
Equations (18), (20) therefore imply
\[
 |d_N(X)|^{\eta/2}N\int_{h_q}^{0}
          \sum_{j=0}^{L_N-1}|T_{j,N}(\beta_N+iv)|\,dv
       \le e^{N\{B^{\rm small}_\eta(x,h)-1/200\}}.
\tag{21}
\]
This estimate does not borrow the weight of the vertical current.

**Corollary 2.** For all sufficiently large levels, uniformly on
(1) and at both parities,
\[
 \boxed{\quad
 |d_N(X)|^{\eta/2}|V_N^{\rm small}(a)|
       \le e^{N\{B^{\rm small}_\eta(x,h)-1/140000\}}.
 \quad}
\tag{22}
\]
Indeed (13), (19), (21) bound every term of the exact identity
(17); their finite sum is absorbed by halving the smallest gap.
This is a bound for the complete finite outgoing sum of the small
retained rows. The central and high retained ranges remain separate,
and the uncompensated marginal is still exactly (15).

## 5. Assembly of the entire finite Fourier boundary function

The central and high retained estimates now complete the upper bound
for the original finite function. To state it with every reference
term fixed, let \(P_\eta\) be as in (15), \(p_\eta=\Re P_\eta\),
and put
\[
\begin{split}
 \chi_0&=1989/4489,\qquad\chi_1=171/196,\\
 B_\eta^{\rm ext}(x)
   &=M_\eta+p_\eta(x-a_R)-\kappa\chi_\eta(x-a_R)^2,\\
 \gamma_\eta(x,h)&=\pi(1-\eta/2)(1/2-x)(h-c),\\
 \mathfrak B_\eta(x,h)
   &=\max\{B_\eta(b),B_\eta^{\rm ext}(x)\}-\gamma_\eta(x,h).
\end{split}
\tag{23}
\]
This is the same baseline as in
[the complete central-source theorem](research_mixed_fourier_right_taper_central_source.md).
Its constants are the original reference constants; there is no
new stationary point or action normalization at the target.

**Corollary 3.** For every fixed \(\tau>0\), there are uniform
constants \(C_\tau,A_\tau,N_\tau\) such that, on (1) and at
both level parities,
\[
 \boxed{\quad
 |d_N(e^{-2\pi ia})|^{\eta/2}
       |V_N^{\rm F}(x_0,e^{-2\pi ia})|
 \le C_\tau N^{A_\tau}e^{N\{\mathfrak B_\eta(x,h)+\tau\}},
                                      \qquad N\ge N_\tau.
 \quad}
\tag{24}
\]

*Proof.* Split the retained index before any estimate:
\[
 V_N^{\rm F}=V_N^{\rm small}+V_N^{\rm cen}+V_N^{\rm hi},
 \qquad
 [0,L_N-1]\ \sqcup\ [L_N,M_N]\ \sqcup\ [M_N+1,N-1].
\tag{25}
\]
Each group contains its complete original outgoing sum. For the
middle group use the central-source theorem. For the first group
use (22). For the last group, the incoming-height theorem gives
the finite bound, after choosing its tolerance,
\[
 |d_N(X)|^{\eta/2}|V_N^{\rm hi}|
 \le C N^A
 e^{N\{B_\eta(b)-(9\pi/25)(h-c)-1/70000\}}.
\tag{26}
\]
On the whole incoming rectangle,
\[
 0\le\gamma_\eta(x,h)\le\frac\pi{20}(h-c)
           \le\frac\pi{10}(h-c)<\frac{9\pi}{25}(h-c)
                         \quad\text{when }h>c,
\tag{27}
\]
and all terms vanish when \(h=c\). Thus the first and last
groups have strictly smaller rates than \(\mathfrak B_\eta\).
Adding the three finite bounds proves (24). \(\square\)

The comparison with the original full complex tangent is still
the explicit expression
\[
\begin{split}
 \mathfrak B_\eta(x,h)-\mathcal L_\eta(x+ih)
 ={}&\Im P_\eta(h-c)-\gamma_\eta(x,h)\\
 &+\max\{-p_\eta(x-b)-\kappa(b-a_R)^2,
                         -\kappa\chi_\eta(x-a_R)^2\}.
\end{split}
\tag{28}
\]
It must be combined with the adjoining ordinary factor and original
boundary compensation. Its sign has not been proved. In particular,
(24) is a complete finite-source upper envelope on the nonpositive
incoming right taper, including its endpoint at \(x=1/2,h=0\).
It is not a lower bound there, a selected-contour estimate, or a
theorem about arbitrary short fillings or closed knot invariants.
