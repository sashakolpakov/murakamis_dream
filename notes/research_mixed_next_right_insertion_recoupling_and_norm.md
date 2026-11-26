# Exact recoupling and the highest coefficient of the right insertion

Private research deduction, 8 November 2026. The coherent insertion in
the closed right paired contour is exactly a projected original
own-four cap followed by the original next transfer. Its highest
ordinary Newton coefficient gives a sharp coefficient lower bound for
every angular strip norm. This identifies an unavoidable exponential
scale on the containing output disks, without deciding the required
action budget at the actual correlated outputs.

The right projection, both Fourier alternatives, the complete forced
weight, and every scalar remain. The vertical and half-grid currents
of the earlier reduction remain separate. No numerical evaluation or
change to a frozen source is used.

## 1. Original conventions and the projected transfer

Use the conventions of
[the right paired terminal insertion](research_mixed_next_right_paired_terminal_insertion.md):
\[
\begin{gathered}
D=N-1,\quad q=e^{\pi i/N},\quad r=q^{-2},\quad
P_j=(r;r)_j,\quad S_j=|P_j|,\quad \kappa=q^{D^2/2},\\
c_j=2\cos((2j+1)\pi/N),\qquad
e_j(t)=S_j^{-2}\prod_{a<j}(c_a-t),\qquad
v(t)=(e_0(t),\ldots,e_D(t))^T,\\
A_3=JM^3,\qquad M=\text{multiplication by the original crossing }\mathcal R_N.
\end{gathered}                                                    \tag{1}
\]
Here \(q\) is the quantum parameter, not a contour coordinate.
The full Frobenius pairing is
\(\phi_N(e_i e_j)=J_{ij}=\mathbf1_{i+j=D}\), including its
repeated-root normals. The crossing values are
\[
\mathcal R_N(c_j)=\kappa(-1)^j q^{j(j+1)},\qquad
|\mathcal R_N(c_j)|=1.                                           \tag{2}
\]

For any set \(I\subset\{0,\ldots,D\}\), let
\[
(\Pi_I F)(X)=\sum_{b\in I}F(r^b)\mathfrak l_b(X),\qquad
\mathfrak l_b(X)=\frac1N\sum_{a=0}^{D}(Xr^{-b})^a .              \tag{3}
\]
This is the original root-cardinal projection. Let
\(U_{1,N}(t,X)\) be the literal cap with first own flag one.
The exact transfer of the
[Fourier message bridge, equation (4)](research_mixed_conditional_fourier_message_bridge.md)
is
\[
\begin{split}
(\mathcal T_{1\beta}F)(Z)
 &=N\operatorname{CT}_X
   [F(X)d_N(X)(1+X^{-N})C_{\beta,N}(X,Z)]\\
 &=\sum_{b=0}^{D}\frac{F(r^b)}{P_b}C_{\beta,N}(r^b,Z),\qquad
\beta=0,1,\\
C_{\beta,N}(X,Z)
 &=\sum_{j=0}^{D}\frac{X^{-j}p_j(X)p_j(Z)}{P_j^{2+\beta}},
\qquad p_j(X)=(rX;r)_j .
\end{split}                                                       \tag{4}
\]
In particular the full polynomial \(d_N\), with
\(d_N(r^b)=P_b^{-1}\), is retained. Neither Fourier summand
in \(1+X^{-N}\) is removed.

Define the coherent projected observation
\[
\mathcal I^I_{\beta,N}(t,Z)
 =\sum_{b\in I}(-q)^b C_{\beta,N}(r^b,Z)(v(t)^TA_3)_b .           \tag{5}
\]
Then the exact recoupling identity is
\[
\boxed{\quad
\mathcal I^I_{\beta,N}(t,Z)
 =\kappa N\,\mathcal T_{1\beta}
               [\Pi_I U_{1,N}(t,\cdot)](Z).
\quad}                                                           \tag{6}
\]

Indeed apply
[the lowered-word identity, Proposition 1](research_mixed_next_lowered_word_dual_observation.md)
to the single-letter word \(4\). Its parameters are
\(m=k=\alpha=1\), so its literal first message is
\(U_{1,N}\) and
\[
U_{1,N}(t,r^b)
 =\kappa^{-1}N^{-1}(-q)^bP_b(v(t)^TA_3)_b .                     \tag{7}
\]
Substitute (7) into (4), with (3). This proves (6) for
arbitrary complex \(t,Z\), as a polynomial identity. In
constant-term notation the right side of (6) has the scalar
\(\kappa N^2\), since (4) already contains one factor \(N\).

For the full set of physical nodes, (6) is simply
\[
\mathcal I^{\rm all}_{\beta,N}(t,Z)
       =\kappa N F_{4,3+\beta,N}(t,Z),                            \tag{8}
\]
where the right side is the original complete two-letter conditional
message. For the right contour the projection is essential:
\[
M_N=\lceil N/2\rceil,\quad B_N=\lceil11N/12\rceil,\qquad
I_N=\{M_N,\ldots,B_N-1\}.                                      \tag{9}
\]
A bound for the full message in (8) gives no bound for the projected
summand in (6).

## 2. Identification with the radical insertion and its top coefficient

The polynomial (5) for (9) is exactly the insertion of equation (19)
in the right paired reduction. To check this before estimating any
coefficient, write
\[
(v(t)^TA_3)_b
 =\phi_N^{(u)}[\mathcal R_N(u)^3e_b(u)K_N^{\rm ord}(t,u)],
\qquad K_N^{\rm ord}(t,u)=\sum_{j=0}^{D}e_j(t)e_j(u).             \tag{10}
\]
For \(b\ge M_N\), the full high-Newton radical contraction
in that source evaluates (10) as
\[
\sum_{j=0}^{D-b}b_{D-b,j}\mathcal R_N(c_j)^3
                                   K_N^{\rm ord}(c_j,t).         \tag{11}
\]
Thus (5) keeps the exact joint \(b,j\) phases of the original
insertion, rather than a positive majorant of its summands.

The Frobenius identity for multiplication gives
\(M^TJ=JM\). Consequently \(JM^3\) is symmetric and
\[
(v(t)^TA_3)_b
 =(M^3v(t))_{D-b}
 =\sum_{j=0}^{D-b}(M^3)_{D-b,j}e_j(t).                           \tag{12}
\]
The lower triangularity here is the exact crossing formula in
[terminal powers, equation (2)](research_terminal_powers_qbinomial.md).
Its diagonal is \(M_{jj}=\mathcal R_N(c_j)\), so
\((M^3)_{jj}=\mathcal R_N(c_j)^3\).

Set
\[
n=D-M_N=\lfloor N/2\rfloor-1 .                                  \tag{13}
\]
For \(N\ge3\), the range (9) includes \(M_N\). Only this
first retained node can contribute to degree \(n\) in (12).
Therefore the coefficient of \(e_n\) in the actual insertion is
exactly
\[
\boxed{\quad
[e_n]\mathcal I_{\beta,N}(t,Z)
 =(-q)^{M_N}\mathcal R_N(c_n)^3
                         C_{\beta,N}(r^{M_N},Z).
\quad}                                                           \tag{14}
\]
This coefficient cannot be canceled by any other retained physical
node. Its modulus is \(|C_{\beta,N}(r^{M_N},Z)|\). As already
proved in the right reduction, the separate degrees in \(t,Z\)
are at most \(n\); if the displayed kernel value vanishes, (14)
simply gives zero and makes no lower-degree assertion.

## 3. Strip lower bounds with both parity constants

For \(h\ge0\), define
\[
\|I\|_h=\sup_{-\pi\le\Re\theta\le\pi,\ |\Im\theta|\le h}
                           |I(-2\cos\theta)| .                  \tag{15}
\]
Put \(w=e^{i\theta}\), so that \(-2\cos\theta=-(w+w^{-1})\).
The leading coefficient of \(e_n(t)\) is \((-1)^n/S_n^2\).
Consequently the coefficient of \(w^n\) in the Laurent polynomial
\(\mathcal I_{\beta,N}(-(w+w^{-1}),Z)\) is the right side of
(14), divided by \(S_n^2\). Cauchy's coefficient formula on
\(|w|=e^h\) proves
\[
\boxed{\quad
\|\mathcal I_{\beta,N}(\cdot,Z)\|_h
 \ge \frac{e^{nh}}{S_n^2}
                         |C_{\beta,N}(r^{M_N},Z)|.
\quad}                                                           \tag{16}
\]
This is a coefficient bound on the complete coherent polynomial;
it does not take a modulus before summing its physical nodes.

There is an exact output test for both own flags:
\[
Z=r^D\quad\Longrightarrow\quad
p_j(Z)=0\ (j\ge1),\qquad C_{\beta,N}(X,r^D)=1.                   \tag{17}
\]
The full sine product \(\prod_{a=1}^{N-1}2\sin(\pi a/N)=N\)
then makes the parity dependence in (16) explicit. If \(N=2m\),
\(n=m-1\) and \(S_n^2=N/2\). If \(N=2m+1\),
\(n=m-1\) and
\(S_n^2=N/[4\cos^2(\pi/(2N))]\). Hence
\[
\|\mathcal I_{\beta,N}(\cdot,r^D)\|_h\ge
\begin{cases}
\displaystyle \frac{2}{N}e^{(N/2-1)h},&N\text{ even},\\[2mm]
\displaystyle \frac{4\cos^2(\pi/(2N))}{N}
                         e^{(N-3)h/2},&N\text{ odd}.
\end{cases}                                                       \tag{18}
\]
At the previously used height \(h=\log2\), these become
\[
\frac{2^{N/2}}N,\qquad
\frac{2^{(N+1)/2}\cos^2(\pi/(2N))}N,
\tag{19}
\]
respectively. Thus a polynomial bound in \(N\) for this strip norm,
uniform on either containing output disk, is impossible. The
physical test (17) lies on the unit circle, which is included in
both disks used for the earlier deletion estimate.

It is not an actual-output counterexample. No assertion places
\(r^D\) in the correlated output image, and no lower bound for
the final terminal trace or for a signed open contour follows from
(16). Nor does (18) contradict an exponential norm budget: that is
the budget the original action comparison requires.

## 4. A smaller strip is sufficient for the terminal operator bound

The source proof of the earlier operator inequality uses trace
contours at heights at most
\[
h_{\rm tr}=2\operatorname{arsinh}\sqrt{(\sqrt2-1)/4},\qquad
\cosh h_{\rm tr}=(1+\sqrt2)/2<5/4=\cosh(\log2).                 \tag{20}
\]
For every fixed \(h>h_{\rm tr}\), the same proof therefore gives
\[
\left|\phi_N[\mathcal R_N^3K_N^{\rm ord}(w,\cdot)I]\right|
 \le C_{\tau,h}N^{A_{\tau,h}}
             e^{N(M_{\rm term}+\tau)}\|I\|_h,
\qquad \deg I\le N.                                             \tag{21}
\]
Indeed the original removed physical wire and angular rows use
Markov bounds for the multiplied polynomial of degree at most
\(2N\). The retained trace surfaces require only finitely many
angular derivatives of the insertion. Cauchy's formula supplies
them using the margin \(h-h_{\rm tr}\). Evenness in the angular
coordinate retains the paired endpoint connectors, and the
insertion remains independent of the private wire coordinate.
Every other physical tail, rational trace charge, alias and
unweighted connector is precisely the complete source inventoried
in Section 4 of the right paired reduction. None is omitted when
the norm height is changed.

There is also a degree-dependent version with only polynomial cost.
For the actual degree (13), set
\[
h_N=h_{\rm tr}+\frac1{n+1}.                                      \tag{22}
\]
For all sufficiently large \(N\), this lies below \(\log2\).
Each fixed angular derivative of order \(k\) now costs at most
\(k!\{2(n+1)\}^k\|I\|_{h_N}\), using a Cauchy radius
\(1/[2(n+1)]\). The degree bounds for physical Markov estimates
are unchanged. Thus (21), with a possibly larger fixed polynomial
power of \(N\), remains valid with \(h=h_N\), uniformly for
\(\deg I\le n\). This modifies only the auxiliary norm estimate,
not the original trace contours or their amplitudes. The original
all-real-color scope and its tolerance-dependent fixed complex
neighborhood of \(-2\) remain those of the source theorem.

Combining this with the exact closed-right reduction gives
\[
|\mathscr R_N^{\rm cl}|
 \le C_\tau N^{A_\tau}e^{N(M_{\rm term}+\tau)}
                     \|\mathcal I_{\beta,N}(\cdot,Z)\|_{h_N}
       +CN^A e^{11N/6}                                           \tag{23}
\]
on the original containing output disks. The second term is the
same positively bounded first-coordinate deletion, not a new
estimate of a signed subset. The lower bound (18) at (22) still
has exponential rate \(h_{\rm tr}/2\) at the test outputs (17).
The narrower strip reduces this explicit benchmark from
\((\log2)/2\); it does not remove exponential growth.

The remaining problem in (23) is an upper bound on the coherent
projected transfer (6) at actual correlated outputs, below the
available original action budget. The exact relation of this
closed rectangle to the desired open horizontal difference still
contains both vertical currents and the even-level half-grid term
from equations (12)--(15) of the preceding reduction. Equations
(6), (16), and (23) estimate none of those terms and make no new
whole-transfer or knot-family assertion.
