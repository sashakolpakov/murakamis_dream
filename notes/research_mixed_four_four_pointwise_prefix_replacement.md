# The complete 44 prefix as a pointwise replacement of its old plateau

Private written corollary, 10 November 2026. The complete first-period
proof gives an exponential replacement before the second retained
coordinate is integrated. Near that coordinate's actual reference,
the literal complete \(44\) message therefore has the original
nonzero \(N^{-5/2}\) packet, with its original action and coefficient.

The proof uses the individual complete-pair bounds underlying the
first-period theorem. It does not deduce a pointwise estimate from
an integrated asymptotic. It completes no second period.

## 1. Exact message and the actual following reference

Fix an actual positive three/four open word of length \(m\ge3\)
beginning with \(44\), with the reference and original logarithmic
lifts of
[the complete first-period theorem](research_mixed_initial44_full_first_period.md).
Write
\[
 r_1=a_1+ic_1,\qquad z_*=r_2=a_2+ic_2,\qquad
 P=[11/50,9/20],\qquad \kappa_0=1/2500000,
\]
\[
 \gamma_L=\kappa_0(a_1-11/50)^2,\qquad
 d_R=\frac{\kappa_0}{2}(9/20-a_1)^2,\qquad
 \gamma=\min\{\gamma_L,d_R\}>0.
 \tag{1}
\]
All heights are fixed at this reference while the ordinary color
and outgoing argument vary. In particular
\(c_1<0\), \(-.102\le c_2\le-.001\), and \(a_2\in P^\circ\).
The actual following Gram leg is \(b_*=s_3^*\). It belongs to
the original ordinary typed domain if vertex three is ordinary,
and to the attached typed domain if \(m=3\). It is not a free
ordinary endpoint or an independently substituted parameter.

Put \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), and retain the literal polynomials
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{j=0}^{N-1}
       H_N(w,q_N^{-j})\,\frac{p_j(X)}{P_j^2},\\
 C_{1,N}(X,Y)&=\sum_{j=0}^{N-1}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^3},\\
 W_{1,N}(X)&=d_N(X)(1+X^{-N}).
\end{split}
 \tag{2}
\]
The endpoint coefficient \(H_N\), diagonal polynomial \(d_N\),
every finite row and both parity conventions remain unchanged.
Define
\[
\begin{split}
 f_{44,N}(w,Y)
 &=N\operatorname{CT}_X
       [U_{1,N}(w,X)W_{1,N}(X)C_{1,N}(X,Y)]\\
 &=\sum_{j=0}^{N-1}
       \frac{U_{1,N}(w,q_N^j)}{P_j}\,C_{1,N}(q_N^j,Y).
\end{split}
 \tag{3}
\]
This is Proposition 1 of
[literal transfer](research_mixed_literal_transfer_norm_obstruction.md).
Before the selected monomial is inserted the \(X\)-band is
\([-N+1,2N-2]\); its only multiples of \(N\) are zero and \(N\).
Thus the \(N\)-scaled sum of those two coefficients equals the
single physical sum in the second line of (3). There is no
additional factor of two. Each \(P_j\), \(j<N\), is nonzero.
The degrees of \(f_{44,N}\) in \(w,Y\) are at most \(N-1\).

For arbitrary complex \(z\), set \(Y=e^{-2\pi iz}\) and define
the exact old unselected plateau message
\[
 I_{44,P,N}(w,z)
   =N\int_{P+ic_1}
       U_{1,N}(w,e^{-2\pi ia})
       d_N(e^{-2\pi ia})
       C_{1,N}(e^{-2\pi ia},Y)\,da .
 \tag{4}
\]
The integration has its original increasing-angle orientation,
with the positive outer density \(N\,da\). Its endpoints and
height are fixed independently of \(w,z\).
It is a polynomial of degree at most \(N-1\) in \(w,Y\).
Write
\[
 R_{44,N}(w,z)=f_{44,N}(w,e^{-2\pi iz})-I_{44,P,N}(w,z).
 \tag{5}
\]

The original first two stationary blocks identify
\(z_*=q_{44}(b_*)\), on the selected sheet of
[the general prefix curve](research_mixed_arbitrary_prefix_pregram_curve.md).
The two-letter instance of
[retained-prefix calibration](research_mixed_retained_prefix_unselected_plateau.md),
Sections 1--2, applies to this actual reference: its inverse-feasible
first44 condition is inherited from vertex two with the following
leg \(b_*\). This includes the attached following leg at \(m=3\).
It does not invoke an isolated two-endpoint \(44\) reference.

## 2. The pointwise complete remainder on the old second plateau

Keep the original allocated first-cap and ordinary phases \(L_1,\phi_2\).
Define, exactly as in the first-period source,
\[
\begin{split}
 M_{12}&=\Re\{L_1(r_1)+\phi_2(r_1,z_*)\},\\
 p_R&=\partial_2\phi_2(r_1,z_*),\\
 \Lambda(y)&=M_{12}+\Re p_R(y-a_2).
\end{split}
 \tag{6}
\]
For \(\sigma=0,1\), put
\[
 K_{\sigma,N}(w;a,z)=
 U_{1,N}(w,X)C_{1,N}(X,Y)d_N(X)X^{-N\sigma},
 \qquad X=e^{-2\pi ia},\quad Y=e^{-2\pi iz}.
 \tag{7}
\]
Only the full first weight occurs in (7); the outgoing halfweight
has not been included in its holomorphic definition.

**Proposition 1.** For every \(\tau>0\), both parities and
\(z=y+ic_2\), \(y\in P\),
\[
 |R_{44,N}(w,z)|\,|d_N(Y)|^{1/2}
 \le C_\tau N^{A_\tau}
                 e^{N\{\Lambda(y)-\gamma+\tau\}} .
 \tag{8}
\]
The bound holds for all \(w\in[-2,2]\), and on a sufficiently
small fixed ordinary-color disk about \(-2\), with a separately
reserved arbitrary allowance. Constants may depend on the fixed
actual word. No uniformity over unbounded word length is claimed.

*Proof.* Use the two complete paths of the first-period theorem:
\[
 \mathcal H_\sigma:\quad
 0\longrightarrow1/10\longrightarrow1/10+iH_\sigma
 \longrightarrow1/2+iH_\sigma\longrightarrow1/2
 \longrightarrow7/10\longrightarrow1,\qquad
 H_0=c_1,\quad H_1=1/100.
 \tag{9}
\]
The point \(9/20+iH_\sigma\) still partitions the horizontal
segment into its original source pieces. Since each integrand
in (7) is entire and one-periodic in \(a\), exact path deformation
and (3) give
\[
 f_{44,N}(w,Y)
       =N\sum_{\sigma=0}^1
                     \int_{\mathcal H_\sigma}K_{\sigma,N}(w;a,z)\,da .
 \tag{10}
\]
This holds for every \(z,w\), not only for physical outgoing
values or after integration in \(z\).

Subtract the unselected plateau piece (4) from (10).
There are exactly the following added oriented currents:

* The six left currents of equation (19) in
  [connected-left assembly](research_mixed_initial44_connected_left_contour.md):
  both real intervals from zero to \(1/10\), their two vertical
  joins, the unselected early horizontal, and the entire selected
  horizontal through \(9/20+i/100\).
* The three right pieces for each \(\sigma\) in equation (4) of
  [connected-right assembly](research_mixed_initial44_connected_right_contour.md),
  from \(9/20+iH_\sigma\) through \(1/2+iH_\sigma\) and \(1/2\)
  to \(7/10\).
* The two real currents from \(7/10\) to one.

Thus the difference has fourteen specified currents, each with
the original positive \(N\,da\) density and its inherited
orientation. The two currents on a common real segment remain
distinct Fourier summands.

For fixed \(z=y+ic_2\), the complete-pair bound (14) and its
table in connected-left assembly bound every first group member
by \(\Lambda(y)-\gamma_L+\tau\), after multiplying by
\(|d_N(Y)|^{1/2}\). Equation (9) of connected-right assembly
bounds every second group member by
\(\Lambda(y)-d_R+\tau\). Corollary 2 of
[the complete real-right pair](research_mixed_initial44_complete_right_real_arc.md)
does the same for the last two currents, including the closed
endpoint one. These are pointwise pair inequalities on the
whole second plateau, before multiplication by any later factor.
All finite cap and conditional rows, their internal currents
and endpoints have already been retained in those inputs.

The path lengths are fixed, and there are finitely many inputs.
Distribute one total allowance among them, integrate their
modulus bounds, and retain the factor \(N\). This proves (8).
The pair inputs have their all-real-color and fixed ordinary-disk
scope, so the same scope holds here by taking their common
constants and disks. In particular no division by a later
conditional or terminal factor has been used to recover (8)
from a whole-word bound. \(\square\)

## 3. Original action and the nonzero plateau packet

Let \(\mathcal T_1(a,w)\) be the original bare first-four cap
action and let \(\psi_1(a,z)\) be the original complete conditional
action. On the original critical branch put
\[
 \mathcal P_{44}(w,z)
   =\operatorname{stat}_a
       [\mathcal T_1(a,w)+\psi_1(a,z)-g(a)] .
 \tag{11}
\]
Here \(g=J+i\pi(z-z^2)/2\) has exactly the original additive
constant and logarithmic lift. Equation (11) is the two-letter
instance of retained-prefix equations (16)--(19), not a new
stationary branch. Its complete-color calibration is
\[
 \mathcal P_{44}(-2,z_*)
              =H_{44}(b_*)-G(z_*,b_*).
 \tag{12}
\]
There is no extra terminal correction at the last letter four.

The outgoing allocated boundary action is
\[
                         L_{44}(z)=\mathcal P_{44}(-2,z)-\tfrac12g(z).
 \tag{13}
\]
At the actual reference, the first internal stationary equation
and the original half allocations give
\[
 \begin{split}
 L_{44}(z_*)&=L_1(r_1)+\phi_2(r_1,z_*),\\
 L_{44}'(z_*)&=\partial_2\phi_2(r_1,z_*)=p_R .
 \end{split}
 \tag{14}
\]
Indeed \(L_1=\mathcal T_1-g(a)/2\) and
\(\phi_2=\psi_1-g(a)/2-g(z)/2\); their sum is precisely
(11) minus \(g(z)/2\). Stationary differentiation removes
the derivative of the internal critical coordinate. Thus
\(\Lambda\) in (6) is the original tangent of \(\Re L_{44}\),
with no new action constant or outgoing weight.

The theorem in Section 4 of retained-prefix calibration gives
fixed neighborhoods of \((-2,z_*)\) on which
\[
 I_{44,P,N}(w,z)=N^{-5/2}\mathcal A_{44}(w,z)
      e^{N\mathcal P_{44}(w,z)}
                (1+O_{\mathrm{hol}}(N^{-1})),\qquad
                    \mathcal A_{44}\ne0 .
 \tag{15}
\]
Its coefficient is exactly its equation (25), with the same
Gaussian branch and complete local cap and conditional symbols.
For clarity the level factors are
\[
 N^{-3/2}\,N^{-1}\,N^{-1/2}\,N\,N^{-1/2}=N^{-5/2}.
 \tag{16}
\]
They are respectively the first-four cap, complete own-four
conditional kernel, internal diagonal polynomial, outer density,
and one-dimensional outer Gaussian. The outgoing halfweight
of (8) is not a factor in (4) or (15).
This is a conditional-prefix normalization, not the
\(N^{-3/2}\) power of the whole terminal-contracted open word.

## 4. Exponential replacement on a fixed outgoing neighborhood

**Theorem 2.** There are fixed complex disks \(B,V\) about
\(-2,z_*\), and constants \(C,\delta>0\), such that
\[
 \left|e^{-N\mathcal P_{44}(w,z)}R_{44,N}(w,z)\right|
                  \le C e^{-\delta N},\qquad (w,z)\in B\times V.
 \tag{17}
\]
One may take \(\delta=\gamma/4\) after shrinking the disks and
increasing the large-level threshold. Every fixed mixed derivative
of the normalized holomorphic expression in (17) has the same
exponential rate on smaller disks. Consequently
\[
 \boxed{\quad
 f_{44,N}(w,e^{-2\pi iz})
 =N^{-5/2}\mathcal A_{44}(w,z)e^{N\mathcal P_{44}(w,z)}
                       (1+O_{\mathrm{hol}}(N^{-1})).
 \quad}
 \tag{18}
\]
The action and nonzero coefficient in (18) are exactly those in
(15), at both parities.

*Proof.* The outgoing plateau segment \(P+ic_2\) is compactly
inside \(0<\Re z<1/2,\Im z<0\). Theorem 1 and equation (19) of
[Fourier-weight continuation](research_mixed_fourier_weight_continuation.md)
give, uniformly on this segment and its sufficiently small
fixed neighborhood,
\[
\begin{split}
 d_N(e^{-2\pi iz})&=f_N(z)(1+O(e^{-cN})),\\
 f_N(z)&=N^{-1/2}\mathcal D(z)e^{-Ng(z)}
                 (1+O(N^{-1})),\qquad \mathcal D(z)\ne0 .
\end{split}
 \tag{19}
\]
This applies on the stated compact segment by the strict
criterion following that theorem, not merely on the smaller
explicit type-four rectangle in its corollary. Thus this
particular outgoing polynomial is zero-free for all sufficiently
large \(N\), with a uniform lower bound given by (19).
Removing only its modulus half from (8) yields, for every
\(\tau>0\),
\[
 |R_{44,N}(w,y+ic_2)|
 \le C_\tau N^{A_\tau}
       e^{N\{\mathcal B(y)-\gamma+\tau\}},\qquad
 \mathcal B(y)=\Lambda(y)+\tfrac12\Re g(y+ic_2).
 \tag{20}
\]
No internal Fourier polynomial, source coefficient, cap,
conditional kernel or terminal transform is divided out.
The extra \(N^{1/4}\) from (19) is included in the polynomial
prefactor.

For each fixed \(w\), (5) is a polynomial of degree at most
\(N-1\) in \(Y=e^{-2\pi iz}\); its plateau endpoints are fixed.
The parameter \(w\) can range over a common closed smaller
disk in Proposition 1. Apply Theorem 1 of
[horizontal complex continuation](research_mixed_horizontal_complex_extension.md)
to (20), treating \(w\) as a compact parameter. The theorem
allows complex coefficients and needs no holomorphic parameter
dependence for its bound. With an arbitrary additional allowance,
it supplies a fixed complex neighborhood of the whole segment
on which (20) persists with its nearby real value \(\mathcal B(y)\).
For example choose the total continuation allowance to be
\(\gamma/8\).

By (14),
\[
                        \mathcal B(a_2)=\Re\mathcal P_{44}(-2,z_*).
 \tag{21}
\]
The source action is holomorphic near this actual reference.
Continuity therefore permits fixed smaller disks \(B,V\) such
that, for \(z\) in the latter disk and its nearby real anchor
\(y+ic_2\),
\[
                   \mathcal B(y)-\Re\mathcal P_{44}(w,z)<\gamma/8.
 \tag{22}
\]
Choose the disks inside the continuation neighborhood and the
packet neighborhood of (15). Equations (20)--(22) bound the
left side of (17) by a polynomial times \(e^{-3\gamma N/4}\).
Absorb that polynomial at the smaller rate \(\gamma/4\).
The expression is holomorphic on a fixed slightly larger
bidisk, so Cauchy's formula gives its fixed mixed derivatives
on smaller disks without differentiating any modulus halfweight.
This proves (17).

The nonzero amplitude in (15) is bounded away from zero after
another shrink. Multiplication of (17) by \(N^{5/2}\) leaves
an exponentially small error relative to that leading symbol.
Adding (17) to (15) proves (18), with the original coefficient
and its original holomorphic relative error. \(\square\)

There is no extra \(\kappa_N\) or outgoing diagonal factor in
(3), (15) or (18). In the terminal-contracted whole-word chart,
substituting (3) changes the original exterior scalar to
\(\kappa_N^{m+k_4}N^{m+k_4-2}\), exactly as in equation (10)
of the first-period theorem. For the next complete contraction,
the full second weight \(d_N(Y)(1+Y^{-N})\) has not been consumed
by this normalization. The current restricted first-period theorem
still uses only its unselected part. For \(m=3\) the remaining
second variable still attaches to the original terminal transform.

## 5. The exact additional requirement at the next period

This section identifies an unproved requirement, not a new
complete-transfer conclusion. For \(\beta\in\{0,1\}\), define
the literal next operation on any polynomial of degree below \(N\):
\[
 (\mathsf T_{1\beta,N}f)(Z)
  =N\operatorname{CT}_Y[f(Y)d_N(Y)(1+Y^{-N})C_{\beta,N}(Y,Z)]
  =\sum_{j<N}\frac{f(q_N^j)}{P_j}C_{\beta,N}(q_N^j,Z).
 \tag{23}
\]
Both coefficient sectors in the first line are retained in its
single physical sum. Put \(F_{44(3+\beta),N}=\mathsf T_{1\beta,N}f_{44,N}\)
and, with \(Y=e^{-2\pi iy}\),
\[
 I_{44(3+\beta),PP,N}(w,z)
   =N\int_{P+ic_2}
       I_{44,P,N}(w,y)d_N(Y)C_{\beta,N}(Y,e^{-2\pi iz})\,dy .
 \tag{24}
\]
This is exactly the two-variable unselected plateau source,
with density \(N^2\) and both full internal diagonal weights.
Linearity of finite polynomials gives the exact remainder identity
\[
\begin{split}
 F_{44(3+\beta),N}(w,e^{-2\pi iz})
     -I_{44(3+\beta),PP,N}(w,z)
 ={}&\mathsf T_{1\beta,N}[R_{44,N}(w,\cdot)](e^{-2\pi iz})\\
 &+\mathsf T_{1\beta,N}[I_{44,P,N}(w,\cdot)](e^{-2\pi iz})
       -I_{44(3+\beta),PP,N}(w,z).
\end{split}
 \tag{25}
\]
In (25) each dotted function is its already defined polynomial
in \(Y\), rather than a new continuation from local values.

For a longer actual word with a third retained coordinate, the
desired next lemma is an exponential bound for the whole left
side of (25), normalized by the original local action
\[
 \mathcal P_{44(3+\beta)}(w,z)
  =\operatorname{stat}_y
       [\mathcal P_{44}(w,y)-g(y)+\psi_\beta(y,z)] .
 \tag{26}
\]
Retained-prefix calibration already gives the nonzero local
packet for (24), of order \(N^{-3-\beta/2}\), and fixes its
absolute action at the actual following leg by
\[
 \mathcal P_{44(3+\beta)}(-2,z_*)
    =H_{44(3+\beta)}(b_*)-G(z_*,b_*)-(1-\beta)g(z_*).
 \tag{27}
\]
Here the starred coordinates in (27) refer to that longer
three-letter prefix, not the two-letter reference of Sections
1--4. They must be identified with the actual word before use.
At total word length three the relevant final operation is
instead the original terminal pairing, not a free next message.

A sufficient new estimate would bound each of the two terms
on the right of (25) below the action (26) by a fixed positive
gap on its actual outgoing neighborhood. Alternatively their
whole signed sum could be bounded without separating them.
Theorem 2 supplies neither estimate: (23) observes a whole
period, including physical values outside its local disk.
The second term also retains the new selected cycle and the
unselected complement of (24), with all connecting currents.

The exact sharp node-norm statement in literal transfer shows
why degree and local jets alone do not supply this step.
A reusable induction would need a global source class whose
error bounds are preserved by (23), with the same reference
correlations, diagonal forcing and action constants. No such
invariant class is asserted here. In particular (18) proves
no completed second period, arbitrary positive word, ordinary
closure or finite-exception theorem.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_initial44_full_first_period.md | 2c7609442313d67b28a5a79374d3712c352fa04092d4756a6f90803ce40cbda7 |
| research_mixed_initial44_connected_left_contour.md | fca8af9ffd728962f97c4e243e19031049a94d001ae83272faaca903479f085e |
| research_mixed_initial44_connected_right_contour.md | cfda9bcc96bb0b0827df17f6bdcc0d7403841f5e6289cf54d80511e99925aa13 |
| research_mixed_initial44_complete_right_real_arc.md | 5ce18a7e361bdb2dc38d67cc9805da0b04361d45c26a06a5c25446599ba814a0 |
| research_mixed_literal_transfer_norm_obstruction.md | e9ce5a518439ed23b94c70eb548470ecbf9abfa5bd7c880f6828ed594a3fe0a3 |
| research_mixed_retained_prefix_unselected_plateau.md | 4f8be2ee4fd0aceda28ad4d96bb4b57d864765438183563c34db070823d6d72b |
| research_mixed_fourier_weight_continuation.md | 0bae41d83f414eb91fd137de1242120a11408147d56ec752e466ca5ed7e7f48e |
| research_mixed_horizontal_complex_extension.md | c7837a9dfb072f2e276f5ccdb99c7421e154a4ca073a078540d8064dbb3747d4 |
| research_mixed_arbitrary_prefix_pregram_curve.md | fb574ec2c0b8f7efe020af4ae3888554fc85040ef444f0c57e7bb8286c14c86c |

The whole written proof and directly used source implications
were read, and all nine bindings were checked. Independent full
proof and direct-source review is required before adoption.
No mathematical numerical evaluation, saved-value arithmetic,
import, test, compilation or frozen-source edit was used.
