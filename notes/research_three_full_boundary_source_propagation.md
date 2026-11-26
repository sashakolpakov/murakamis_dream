# The complete Fourier boundary function of a three-crossing chain

Research deduction, 7 November 2026. The manuscripts are unchanged.

The existing induction bounds the entire real boundary period, but
its repeated attachment uses a matrix with a small corner removed.
The corner estimate is strong enough to restore the original matrix
at every length while preserving the same boundary estimate and
nonzero local asymptotic. Thus the actual homogeneous chain, not
only its truncated counterpart, belongs to the proved boundary
class. This deduction uses existing inequalities; it requires no
new numerical evaluation.

## 1. The two finite functions

Keep the original matrices and boundary vectors. Write
\[
 A_N=JM^3,\qquad
 \widetilde A_N=A_N-E_{\lfloor N/40\rfloor},\qquad
 x_h=\frac16+\frac{i\log2}{2\pi},\qquad
 k_0=\frac{4\pi}{21}(2\sqrt3-3i).
 \tag{1}
\]
The removed matrix in (1) is exactly the cutoff used in
[the larger-source induction](research_three_larger_source_propagation.md).
For each fixed integer \(m\ge3\), set
\[
 \begin{split}
 F_{m,N}(y,w)&=v(w)^TA_N^mh(y),\\
 \widehat F_{m,N}(y,w)
   &=v(w)^TA_N^3\widetilde A_N^{\,m-3}h(y),\\
 R_{m,N}&=F_{m,N}-\widehat F_{m,N}.
 \end{split}
 \tag{2}
\]
All three expressions are literal finite functions at both level
parities. In particular their definition does not involve a local
approximation of a boundary vector.

Let \(S_m\) and \(a_m\) be the phase and nonzero amplitude of
\(\widehat F_{m,N}\) from Corollary 2 of the induction theorem.
At complete ordinary color define
\[
 \begin{gathered}
 M_m=\Re S_m(x_h,-2),\qquad
 H_m=Z^{m-3}\frac{57}{10000},\qquad A=\frac{29}{20},\\
 Z=\frac{(21/20)\rho}{1-(3/10)\rho},\qquad
 \rho=\frac{5-\sqrt{21}}2,\\
 \mathcal U=\{|z|\le1/200\}\cup[-9/1000,9/1000],\qquad
 v(t)=\min\{\operatorname{dist}(t,\mathbb Z),3/100\}.
 \end{gathered}
 \tag{3}
\]
The known bound \(0<Z<1\) gives \(H_m\le57/10000\).
The source theorem supplies, uniformly on \(z\in\mathcal U\),
\[
 \begin{split}
 \widehat F_{m,N}(x_h+z,-2)
   &=C_{N,3}\kappa^{m-1}N^{-1}a_m(x_h+z,-2)
        e^{NS_m(x_h+z,-2)}(1+O(N^{-1})),\\
 \frac{\partial_y S_m(x_h+z,-2)}{k_0}
   &=-\sqrt{21}z+g_m(z),\qquad
       |g_m(0)|\le H_m,\quad |g_m'|\le\frac9{50},\\
 |\widehat F_{m,N}(x_h+t,-2)|
   &\le C_mN^{b_m}
      e^{N\{M_m+|k_0|H_mv(t)-Av(t)^2\}},\qquad t\in\mathbb R.
 \end{split}
 \tag{4}
\]
The first line retains its original carriers. Each fixed ordinary
outside-color jet has the differentiated local expansion and the
same real-period exponential bound, with a possibly larger power of
\(N\). This is a statement at \(w=-2\); it does not assert a
global envelope on a fixed complex neighborhood of that color.

## 2. A uniform exponential margin for restoring the corners

**Lemma 1.** For every fixed \(m\ge3\) and fixed nonnegative
integers \(a,b\),
\[
 \sup_{t\in\mathbb R}
 |\partial_w^a\partial_y^bR_{m,N}(x_h+t,-2)|
 \le C_{m,a,b}N^{B_{m,a,b}}
                e^{N(M_m-19/100)}.
 \tag{5}
\]
The constants and the threshold in \(N\) may depend on \(m,a,b\).

*Proof.* Theorem 2 and Section 4 of
[the Fourier corner estimate](research_three_chain_fourier_corner_transfer.md)
apply to any word whose factors are either \(A_N\) or the same
\(\widetilde A_N\) as in (1). They therefore apply to (2),
with the exponent
\[
 r_m=(2m-2)c+\frac{M_\infty}{2}
                         +\frac{27}{200}+\frac{\log2}{2}.
 \tag{6}
\]
Here \(c=2\mathcal J(5/6)\) and
\(M_\infty=4G/\pi\) have their original definitions; \(G\)
is Catalan's constant. The same proof establishes
\[
 r_2<\frac{343}{200},\qquad r_m=r_2+2(m-2)c.
 \tag{7}
\]
No new estimate of these constants is required.

Write \(M_{\mathrm{prep}}=\Re S_1(x_h,-2)\) for the
two-vertex prepared source of
[the real-output theorem](research_three_prepared_cap_real_extension.md).
That theorem gives \(M_{\mathrm{prep}}>19113/10000\).
Equation (7) of
[the first-entrance extension](research_three_first_entrance_real_extension.md)
and equation (16) of the larger-source induction give, respectively,
\[
 M_3>M_{\mathrm{prep}}+2c-\frac{66}{10^6},\qquad
 |M_m-M_3-2(m-3)c|<\frac6{10^6}.
 \tag{8}
\]
For \(m=3\), the second difference is zero. Hence
\[
 M_m-r_m>
 \frac{19113}{10000}-\frac{343}{200}-\frac{72}{10^6}
 =\frac{196228}{10^6}>\frac{19}{100}.
 \tag{9}
\]
The corner theorem retains all fixed ordinary and Fourier derivatives
and is uniform over the real Fourier period. This proves (5).
\(\square\)

## 3. The original chain satisfies the same boundary estimates

**Theorem 2.** Replace \(\widehat F_{m,N}\) by \(F_{m,N}\)
in the first and third lines of (4). Both conclusions remain valid,
with the same phase, leading amplitude, carriers, and parameters
\(M_m,H_m,A,v\). Their fixed ordinary-jet scope also remains
unchanged. In particular the leading amplitude of the original
finite function is nonzero on the local output domain.

*Proof.* First consider the entire real period. Its envelope exponent
is bounded below by
\[
 M_m+|k_0|H_mv(t)-Av(t)^2
 \ge M_m-\frac{29}{20}\left(\frac3{100}\right)^2
 >M_m-\frac1{500}.
 \tag{10}
\]
Consequently (5) is exponentially below that envelope, uniformly in
\(t\). Adding \(R_{m,N}\) changes only its polynomial
prefactor. The same reasoning applies to each fixed ordinary jet.

For the local asymptotic, a point \(z\in\mathcal U\) can be
joined radially to zero within the same component of \(\mathcal U\).
Since \(|k_0|<3\), \(\sqrt{21}+9/50<5\), and
\(|z|\le9/1000\), integration of the second line of (4) gives
\[
 \begin{split}
 |S_m(x_h+z,-2)-S_m(x_h,-2)|
 &\le3\left\{\frac{57}{10000}|z|+\frac52|z|^2\right\}\\
 &\le\frac{7614}{10^7}<\frac1{1000}.
 \end{split}
 \tag{11}
\]
Moving the Fourier output off the real period by height
\(\Im z\) adds at most \(\pi|\Im z|\) to the error
exponent in the corner theorem. On the disk in \(\mathcal U\),
this is at most \(\pi/200<2/125\); on its real interval it
is zero. Thus, on all of \(\mathcal U\),
\[
 |R_{m,N}(x_h+z,-2)|
 \le C_mN^{B_m}
    e^{N\{\Re S_m(x_h+z,-2)-17/100\}}.
 \tag{12}
\]
Indeed (5), (11), and the height cost leave a gap strictly greater
than \(19/100-2/125-1/1000=173/1000>17/100\).
The error is therefore negligible relative to the nonzero first
term in (4), including its factor \(N^{-1}\).

All margins are strict. On a sufficiently small neighborhood of
the compact output domain, the same comparison follows from the
holomorphic phase and the height estimate. The original corner
estimate supplies all fixed ordinary jets as well. Adding their
errors preserves the differentiated local asymptotics inherited
from (4). This does not assert that each individual derivative has
a nonzero leading coefficient, or enlarge the ordinary-color
domain of the original propagation theorem. \(\square\)

## 4. What this permits in a composition argument

The cardinal identity gives the exact original attachment
\[
 F_{m+1,N}(y,w)=N\int_{x_h-1/2}^{x_h+1/2}
       F_{m,N}(x,w)\,h(x)^TA_Nh(y)\,dx.
 \tag{13}
\]
Theorem 2 shows that the actual sequence in (13), starting at
\(m=3\), stays in the same class of local asymptotics and
global real-period bounds as the retained sequence. Its central
phase derivative contracts according to \(H_{m+1}=ZH_m\).
The additive action constants are the original ones from stationary
composition; they have not been replaced by homogeneous increments.

This is an assertion about these actual complete-ended functions.
It is not an operator theorem for every function satisfying the
three bounds in (4): the corner proof uses the original finite
matrix word and its original left boundary vector. Nor does it
establish stability under a type-four attachment. An exact change
of basis may now transfer this full homogeneous family to another
boundary representation without leaving unestimated deleted
corners. Establishing the corresponding analytic class across a
mixed interface remains necessary.

No length growing with \(N\), new knot class, or general
finite-exception theorem is claimed.
