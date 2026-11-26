# Conditional propagation through an adjacent bare hub

Private formulation, 1 November 2026. No public extension is claimed.

The all-parity low-array trace comparison preserves a useful part of the original source through another bare product junction. It does not, by itself, propagate an arbitrary positive spectral error gap. The exact missing budget can be stated and proved without assuming that intrinsic branch pressures add at an arbitrary cut.

## 1. An input invariant with the original coefficient profile

Let a bare hub have \(B\ge2\) children of strict types L or A. For each child choose its original positive complete reference polynomial
\[
 Q^0_{i,N}=\sum_{r=0}^{d}q^0_{i,N,r}e_r,
 \qquad q^0_{i,N,r}\ge0,
\]
with its absolute boundary action \(f_i(x)\). All constants accumulated in its original subtree are included. Put
\[
 \Omega_i=\max_{0\le x\le1/2}\{f_i(x)+g(x)\}.
 \tag{1}
\]
Suppose the actual deformed child has an exact decomposition
\[
 Q_{i,N}(s)=C_{i,N}(s)+E_{i,N}(s),
 \tag{2}
\]
where \(C_i\) has only low Newton coordinates and satisfies
\[
 |[e_r]C_i|\le\exp\{No(1)\}q^0_{i,N,r}\quad(r\le M),
 \qquad
 \|E_i\|_{\mathrm J}\le\exp\{N(\Omega_i-\gamma_i+o(1))\},
 \quad\gamma_i>0.
 \tag{3}
\]
An identically zero error can be assigned \(\gamma_i=+\infty\). The first comparison is with the actual old child profile; it does not replace an A child by \(g+c\). All statements are uniform on a fixed \(|s|\le R<1\) and over the remaining prescribed color parameters.

Let
\[
 A^0_N=\prod_i^{*_0}Q^0_{i,N},\qquad
 Q^0_{v,N}=T_0 A^0_N,
\]
and let \(f_A\) be the original optimized profile of the unturned product. The parent's intrinsic pressure is
\[
 \Omega_v=\max_{0\le x\le1/2}\{f_A(1-x)+g(x)\}.
 \tag{4}
\]
We will prove the exact pressure identity and inequality
\[
 \Omega_A:=\max_{0\le x\le1/2}\{f_A(x)+g(x)\}
       =\sum_i\Omega_i,\qquad
 \Delta_v:=\Omega_v-\sum_i\Omega_i\ge0.
 \tag{5}
\]
The inequality is strict if at least one child is A, or if \(B\ge3\). The exceptional two-L-child case has equality.

## 2. Why the particular pressures in (5) are additive

At every odd level the complete node \(-2\) is simple. High Newton polynomials vanish there, and low Newton polynomials are positive. Thus for each of the original positive reference polynomials,
\[
 Q^0_{i,N}(-2)=\sum_{r\le M}q^0_{i,N,r}e_r(-2)>0.
 \tag{6}
\]
The positive coefficient Laplace principle and the uniform low-basis rate \(g\) give
\(N^{-1}\log Q^0_{i,N}(-2)\to\Omega_i\).
The exact quotient evaluation is multiplicative at this root:
\[
 A^0_N(-2)=\prod_iQ^0_{i,N}(-2).
 \tag{7}
\]
Since the complete product also has nonnegative canonical Newton coefficients, the left side has rate \(\Omega_A\). Equations (6)--(7) prove the equality in (5). These are the original parity-independent action profiles; an identity between their variational values proved along odd levels is consequently an identity of those profiles, not a change of the physical even level.

This additivity concerns one unturned product evaluated at its common intrinsic probe \(-2\). It is not an assertion that the pressures of arbitrary branches cut from a larger diagram sum to that diagram's action. In particular it does not remove the cap/gluing terms identified in the earlier pruning budget.

For the inequality, resolve the last product as \(A=FG\), with strict L/A children, and use the original unsquared product equations. They give
\[
 f_A'(z)\ge f_{hh}'(z)\quad(0<z<1),
 \tag{8}
\]
strictly if a child of that last gate is A. The additive constants do not affect (8). The two-leaf profile obeys
\(f_{hh}(z)=f_{hh}(1-z)\). Integration between \(x\) and \(1-x\) therefore gives
\[
 f_A(1-x)\ge f_A(x)\quad(0<x<1/2).
 \tag{9}
\]
When \(B\ge3\), group all but one child first; that grouped product is A. If one of two children is already A, the inequality is also strict. The original strict probe has an interior maximizing leaf index. Evaluating (9) there gives the strict form of (5) in those cases. If the two children are L, their profiles are \(g+c_1,g+c_2\), so \(f_A=f_{hh}+c_1+c_2\), and the pressures are equal. This checks the sign of \(\Delta_v\) from the actual source geometry.

## 3. The clean-low part survives another bare turn

Form the actual parent
\[
 Q_{v,N}(s)=\mathscr T_s\left(\prod_i^{*_\sigma}Q_{i,N}(s)\right),
 \qquad \sigma\in\{s,0\}
\]
in its prescribed oriented type. Define its clean part by
\[
 C_{v,N}(s)=\Pi_{\mathrm{lo}}\,mathscr T_s
                  \left(\prod_i^{*_\sigma}C_{i,N}(s)\right).
 \tag{10}
\]
For a low output \(r\), the exact coefficient extractor inserts the low probe \(e_r\). The all-parity trace comparison applies because every factor in (10) is low. Its paired turn factor is bounded on the chosen disk. Hence
\[
 |[e_r]C_v|
 \le \exp\{No(1)\}
 [e_r]T_0\left(\prod_i^{*_0}(Q^0_{i,N})^{\mathrm{lo}}\right)
 \le\exp\{No(1)\}q^0_{v,N,r}.
 \tag{11}
\]
The last step uses positivity of the complete multiplication, trace and reversal. It introduces no physical alias identity. Thus the correct old low-coordinate majorant propagates even when the child profiles are not rigid.

The coefficient majorants also imply
\[
 \|C_i\|_{\mathrm J}\le\exp\{N(\Omega_i+o(1))\}.
 \tag{12}
\]
For the high output of the all-clean product, the exact trace extractor has a high probe, and both that probe and the output high basis have polynomial spectral norm. Fixed-valence quotient folding therefore gives
\[
 \left\|\Pi_{\mathrm{hi}}\mathscr T_s\prod_iC_i\right\|_{\mathrm J}
       \le\exp\left\{N\left(\sum_i\Omega_i+o(1)\right)\right\}.
 \tag{13}
\]
By (5), this sector has a strict loss \(\Delta_v\) whenever the parent has an A child. This part of the adjacent-hub step is already closed.

## 4. The exact condition for a spectral error alone

Expand the difference between the actual product and the all-clean product by nonempty error subsets \(S\subset\{1,\ldots,B\}\). Let
\[
 R_S=\prod_{i\in S}^{*_\sigma}E_i
                  *_\sigma\prod_{i\notin S}^{*_\sigma}C_i.
\]
The signed product is kept intact. Polynomial folding gives
\[
 \|R_S\|_{\mathrm J}
 \le\exp\left\{N\left(\sum_i\Omega_i-
                      \sum_{i\in S}\gamma_i+o(1)\right)\right\}.
 \tag{14}
\]
For a high output, the probe and reconstruction have only polynomial cost, so
\[
 \|\Pi_{\mathrm{hi}}\mathscr T_sR_S\|_{\mathrm J}
 \le\exp\left\{N\left(\sum_i\Omega_i-
                      \sum_{i\in S}\gamma_i+o(1)\right)\right\}.
 \tag{15}
\]
For a low output, the inserted \(e_r\) costs at most \(e^{NG_0+o(N)}\), and reconstruction against the low basis costs a second such factor. Thus
\[
 \|\Pi_{\mathrm{lo}}\mathscr T_sR_S\|_{\mathrm J}
 \le\exp\left\{N\left(\sum_i\Omega_i-
                      \sum_{i\in S}\gamma_i+2G_0+o(1)\right)\right\}.
 \tag{16}
\]
These two costs arise at the new turn. They cannot be deleted merely because the input error had a strict spectral loss.

Put \(\gamma_* =\min\{\gamma_i:E_i\ne0\}\), with \(\gamma_*=+\infty\) if all errors vanish. Define
\[
 \Gamma_v=\min\{\Delta_v,\ \Delta_v+\gamma_*-2G_0\}.
 \tag{17}
\]
Equations (13)--(16), and the fixed number of subsets, prove the following conditional propagation statement:

> If \(\Gamma_v>0\), then the exact parent decomposition
> \(Q_v=C_v+E_v\), with \(C_v\) defined in (10), satisfies (11) and
> \(\|E_v\|_{\mathrm J}\le\exp\{N(\Omega_v-\Gamma_v+o(1))\}\).

Any fixed smaller positive gap can absorb the uniform errors and polynomial factors. In particular, at an adjacent bare-hub step, where \(\Delta_v>0\), a sufficient condition is
\[
                         \boxed{\ \gamma_*+\Delta_v>2G_0.\ }
 \tag{18}
\]
The proof establishes \(\Delta_v>0\), but not (18). The earlier whole-hub theorem supplies a positive gap, not a universal gap as large as \(2G_0-\Delta_v\). Thus it cannot be iterated by referring only to the word “strict.” Failure of this sufficient inequality is not a lower bound for a signed error and is not a counterexample to the desired source theorem.

## 5. What a stronger error invariant would have to retain

A possible improvement is to retain a positive low-coordinate envelope for each error, together with a separate high/remainder budget. The all-parity trace comparison applies to arbitrary low arrays, so it can use an error's actual low profile rather than replacing its entire norm by the worst-case two-basis cost in (16).

Precisely, for nonnegative low arrays \(a_i\) define the old positive functional
\[
 \mathcal P_N(a_1,\ldots,a_B)
   =\sum_{r\le M}e_r(-2)\,
          \phi_0\left(e_r\prod_i\sum_{n\le M}a_{i,n}e_n\right).
 \tag{19}
\]
It is the exact positive low-output reconstruction bound, with all original shared indices. If a dirty low input has coefficient profile \(e_i(x)\), the corresponding exponential rate is the constrained old pressure obtained by substituting that profile in (19). The required improvement is a strict inequality between each such mixed pressure and \(\Omega_v\), together with a compatible estimate for terms containing a high remainder. These are statements about the coupled old source, not independent maxima assigned to each edge.

Nothing here proves those inequalities for general adjacent bare hubs. Equations (11), (13), and (17)--(18) isolate what is already rigorous and the exact additional budget required by the simpler spectral-error invariant. The current public source class remains unchanged.
