# A whole first-collar bound for every two-vertex mixed word

Research deduction, 5 November 2026. A uniform finite collar estimate
for either complete terminal transform follows from the original
conditional product bound and the coherent endpoint row sum. Its
ceiling is sufficient for every length-two word with types three or
four after retaining the type-four action credits. This proves a
discarded-sector upper bound, not dominance on the rest of the period.
No root, source evaluation or new numerical comparison is used.

## 1. An exact seam identity and a separate collar estimate

Use the literal polynomials and normalization of
[reversed-cap assembly](research_mixed_reversed_cap_assembly.md):
\[
 \begin{split}
 C_{\beta,N}(X,Y)
 &=\sum_{i<N}\frac{X^{-i}p_i(X)p_i(Y)}{P_i^{2+\beta}},\\
 V_{\beta,N}(w,X)
 &=\sum_{j<N}C_{\beta,N}(X,r^j)
                       \frac{H_N(w,r^{-j})}{P_j^\beta},
 \qquad \beta=0,1.
 \end{split}
 \tag{1}
\]
Every finite row, ordinary color and level parity is retained.
For the type-three transform there is also the exact identity
\[
                         V_{0,N}(w,1)=N U_{1,N}(w,1).
 \tag{2}
\]
Indeed its original transform formula gives
\(V_0(w,1)=\sum_{i<N}U_0(w,r^i)\), since \(p_i(1)=P_i\).
The polynomial \(U_0(w,Z)\) has degree less than \(N\), so this
root sum is \(N[Z^0]U_0\). The exact cap formula (17) of
[conditional composition](research_mixed_conditional_torus_composition.md)
identifies that constant coefficient as
\(\sum_j H_N(w,r^{-j})/P_j=U_1(w,1)\).
This proves (2), including all ordinary derivatives. It is only a
seam identity; no identity of the neighboring polynomials is inferred.

For the collar estimate put
\[
 \begin{split}
 b_0=101/125,\qquad b_1=433/500,\qquad
 \Delta_\rho=\rho\log2-J(\rho),\qquad \nu_\rho=-J(\rho),\\
 L(u)=-2J((1-u)/2),\qquad
 M_\beta(0)=\max_{0\le u\le1}\{L(u)-(1+\beta)J(u)\}.
 \end{split}
 \tag{3}
\]
For \(0<\rho\le1/1000\), both collar costs tend to zero as
\(\rho\downarrow0\). The already proved strict scalar bounds are
\[
                    M_0(0)<163/500,\qquad M_1(0)<7/15.
 \tag{4}
\]
The first is (12) of the
[three-cap collar comparison](research_mixed_three_cap_collar_comparison.md).
The second is the bound \(M_1(0)+1/12<11/20\) in the proof of
Theorem 1 of the [full boundary-strip estimate](research_mixed_boundary_strip_bounds.md).
Neither scalar is recomputed here.

**Lemma 1.** For every prescribed \(\eta>0\), on a sufficiently
small fixed ordinary-color disk, uniformly for \(0\le x\le\rho\),
\[
 |V_{\beta,N}(w,e^{-2\pi ix})|
 \le C_\eta N^{A_\eta}
       \exp N\{b_\beta+M_\beta(0)+\Delta_\rho+\eta\}.
 \tag{5}
\]
This holds at all sufficiently large integer levels of either parity
and for every fixed ordinary derivative on a smaller disk.

*Proof.* Write \(S_i=|P_i|\). The zero-safe real collar estimate
(7) of [the real-collar proof](research_mixed_real_zero_collar.md)
gives, for every \(i<N\),
\[
 \frac{|p_i(e^{-2\pi ix})|}{S_i}
                  \le C N^A e^{N\Delta_\rho}.
 \tag{6}
\]
The all-period product estimate (6) of the boundary-strip proof gives
\(|p_i(Y)|\le N^A e^{NL(i/N)}\) for every \(|Y|=1\).
Since the first chirp has modulus one, the literal sum in (1) and
the all-index sine-factorial bound imply
\[
 \sup_{|Y|=1}|C_{\beta,N}(e^{-2\pi ix},Y)|
 \le C N^A e^{N\{M_\beta(0)+\Delta_\rho\}}.
 \tag{7}
\]
The endpoint and upper rows are included in these product bounds.

The whole coherent coefficient satisfies
\(H_N(w,r^{-j})=P_j D_N(j/N)^{-1}\mathcal C_N(j/N,w)\),
where \(|D_N(j/N)|=1\). Hence Theorem 1 of
[the cap seam source bound](research_mixed_cap_seam_source_bounds.md)
is exactly the positive row bound
\[
 \sum_{j<N}\frac{|H_N(w,r^{-j})|}{S_j^\beta}
 =\sum_{j<N}|\mathcal C_N(j/N,w)|S_j^{1-\beta}
 \le C_\eta N^{A_\eta}e^{N(b_\beta+\eta)}.
 \tag{8}
\]
It keeps the entire Newton polynomial within each coefficient and
is uniform through both physical endpoints, both parities and small
ordinary-color disks. Apply (7)--(8) to (1). This proves (5).
Taking a triangle bound in the remaining private index is legitimate
here; the result is used only near the incoming seam, not near its
geometric critical value. Cauchy's formula gives the fixed ordinary
derivatives. \(\square\)

The derivation of (5) is independent of (2). In particular it does
not extend a cancellation at one point by an \(N\)-dependent
continuity neighborhood.

## 2. A type-four action credit at every attached endpoint

Let \(z=x+ih\) be an attached type-four endpoint leg. The proved
[endpoint rectangles](research_mixed_open_word_endpoint_rectangles.md)
give
\[
                  .246<x<.350,\qquad -.108<h<-.020.
 \tag{9}
\]
Then
\[
                              -\Re g(z)>1/20.
 \tag{10}
\]
To prove it set \(\theta=2\pi x\), \(R=e^{2\pi h}\), and
\(A_\theta(r)=\arg(1-r e^{-i\theta})\), \(0\le r\le R\).
The argument has its original right-half-plane lift. Here
\(\sin\theta>4/5\) and \(1/2<R<1\). For the radial bound,
\(.216\pi<17/25\) and
\[
 e^x\le1+x+\frac{x^2}{2(1-x/3)}<2
                    \quad(x=17/25)
\]
prove \(R>1/2\). The sine bound follows from
\(\theta\in(.492\pi,.7\pi)\) and the existing elementary
\(\sin(.7\pi)>4/5\).
Since
\[
 A_\theta'(r)=\frac{\sin\theta}{1-2r\cos\theta+r^2}
              \ge\frac{\sin\theta}{(1+r)^2},
 \tag{11}
\]
integration gives \(A_\theta(r)\ge r\sin\theta/(1+r)\).
The prescribed primitive has \(\Re g\to0\) at radial zero,
and therefore
\[
 -\Re g(z)
 =\frac1{2\pi}\int_0^R\frac{A_\theta(r)}r\,dr
 \ge\frac{\sin\theta}{2\pi}\log(1+R)
 >\frac4{25\pi}>\frac1{20}.
 \tag{12}
\]
We used \(\log(3/2)>2/5\) and \(\pi<22/7<16/5\).
All estimates are analytic scalar inequalities.

## 3. The actual two-vertex action pays the seam ceilings

Fix the word \((3+\alpha,3+\beta)\), \(\alpha,\beta\in\{0,1\}\).
Let \(a=t_1^*\) be its retained coordinate and \(t=s_2^*\) its
opposite attached leg. The original calibrated action is
\[
 \begin{split}
 M_{\rm open}
 &=\Re\{\mathcal T_\alpha(a,-2)+P_\beta(a)-\alpha g(a)\}\\
 &=\Re\{\mathcal T_\alpha(a,-2)+\mathcal T_\beta(t,-2)
                 +W(t,a)-\alpha g(a)-\beta g(t)\},\\
 W(t,a)&=J(t+a)-J(t)-J(a)+i\pi at.
 \end{split}
 \tag{13}
\]
This is the exact two-factor specialization of the original contracted
source; no conditional factor remains. The two cap floors exceed one.
The [terminal floor proof](research_mixed_terminal_transform_tails.md),
Lemma 1, also gives \(\Re P_\beta(a)>107/100\), and proves
on these endpoint ranges
\[
 \Re W(t,a)>1/5-\pi\{(\Re t)(\Im a)+(\Re a)(\Im t)\}.
 \tag{14}
\]
Its real floor and vertical-convexity argument include length-two
mutually attached endpoints. No ordinary-block height is substituted
for an endpoint height.

For \(\beta=0\), (13) gives \(M_{\rm open}>207/100\):
the first cap exceeds one, and the first type-four weight, when
present, contributes a positive credit. For \((\alpha,\beta)=(0,1)\),
one has \(\Im t<0\), \(\Re t<.350\), and
\(\Im a<.021\). Equations (10), (13)--(14) give
\[
                    M_{\rm open}>9/4-147\pi/20000.
 \tag{15}
\]
For \((\alpha,\beta)=(1,1)\), both attached heights are negative.
Thus \(\Re W>1/5\), both credits in (10) apply, and
\(M_{\rm open}>23/10\).

The original finite ceiling at the seam is
\(b_\alpha+b_\beta+M_\beta(0)\). The preceding strict bounds
give the following rational comparisons:
\[
\begin{array}{c|c|c}
 (\alpha,\beta)&\text{source ceiling is less than}
                         &\text{reference action is greater than}\\\hline
 (0,0)&971/500&207/100\\
 (1,0)&2&207/100\\
 (0,1)&3211/1500&9/4-147\pi/20000\\
 (1,1)&1649/750&23/10.
\end{array}
 \tag{16}
\]
Every right entry minus its middle entry exceeds \(7/100\).
For the third entry this follows directly from \(\pi<22/7\);
the other comparisons are rational. This is the needed calibration
of the positive ceiling; no bound is inferred from its size alone.

## 4. The full two-vertex collar, all original selections

The exact contracted integrand is
\[
 \mathscr J_N(X)=U_{\alpha,N}(w_L,X)V_{\beta,N}(w_R,X)
                      d_N(X)^\alpha X^{-N\sigma},
 \qquad \sigma\in\{0,\alpha\}.
 \tag{17}
\]
On the actual first collar \(X=e^{-2\pi ix}\), \(0\le x\le\rho\),
the target height is zero and the selected monomial has modulus one.
This is literal for the
[split hybrid graph](research_mixed_split_cutoff_hybrid_contour.md),
Section 2, equations (2)--(4): \(R_\varepsilon(x)L_b(x)=0\)
on \([0,.1]\), so the own-coordinate factor forces height zero
for either the unselected base height or the selected base \(7/500\).
The [open-chain convention](research_mixed_open_boundary_comparison_reduction.md),
Section 1, assigns cutoff one to missing neighbors. Thus the same
statement includes the single retained coordinate when \(m=2\).
The cap seam theorem gives the first-factor ceiling
\(b_\alpha+\Delta_\rho\). The forced Fourier recurrence in
the real-collar proof, with its \(L\) replaced by the fixed \(\rho\),
gives the full weight ceiling
\(\alpha\nu_\rho\), uniformly including \(x=0\).
Together with (5), their rate is at most
\[
        b_\alpha+b_\beta+M_\beta(0)
                        +2\Delta_\rho+\alpha\nu_\rho+\eta,
 \tag{18}
\]
where \(\eta>0\) is a single total finite-source/color tolerance.

Choose a fixed collar so that
\(2\Delta_\rho+\nu_\rho<1/100\), and then choose
\(\eta<1/100\). Equation (16) proves:

**Theorem 2.** For every fixed two-vertex mixed word, both first
selections, all sufficiently large integer levels of either parity,
and fixed sufficiently small ordinary-color disks at both ends,
\[
            |\mathscr J_N(e^{-2\pi ix})|
             \le C N^A e^{N(M_{\rm open}-1/20)}
                     \qquad(0\le x\le\rho).
 \tag{19}
\]
Every fixed pair of ordinary derivatives has the same rate on smaller
disks. The terminal polynomial remains whole, including its original
private Fourier alternatives. Integrating this sector and multiplying
by the exact original scalar
\(\kappa_N^{2+\alpha+\beta}N^{1+\alpha+\beta}\) preserves the
exponential gap, with a polynomial prefactor.

This supplies the length-two first-collar sector which is outside the
terminal plateau domain. It neither moves a plateau theorem to zero
nor assumes a moving endpoint critical point. The other target angles,
nonplateau transitions, and whole ordinary-closure asymptotic remain
separate obligations. No one-vertex formula is included.
