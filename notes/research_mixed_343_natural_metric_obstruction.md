# The natural positive metric for the exact 343 transfer

Private research deduction, 8 November 2026. The two original
sampled Fourier coefficients have one exact positive-Gram operator
representation. Its remaining crossing cannot be placed in a fixed
complex half-plane by the natural metric induced by that Gram
operator. This is an obstruction to a global numerical-range
argument, not to a cone containing only the actual source or to
the desired particular transfer estimate. No numerical evaluation
or change to a frozen source is used.

## 1. The complete two-coefficient observation

Retain the original Newton crossing \(M\), reversal \(J\),
ordinary evaluation column \(v(w)\), and scalars
\[
 D=N-1,\qquad q=e^{\pi i/N},\qquad r=q^{-2},\qquad
 \kappa=q^{D^2/2},\qquad A_n=JM^n.
 \tag{1}
\]
Put
\[
 H=M^*M>0,\qquad
 U=\operatorname{diag}((-q)^{-j})_{j=0}^{D},\qquad
 \mathfrak l_b(Z)=\frac1N\sum_{k=0}^{D}(Zr^{-b})^k,
 \qquad g(Z)=U^*\mathfrak l(Z).
 \tag{2}
\]
The column \(g(Z)\) is the prescribed polynomial observation;
it is not replaced by an adjoint of the incoming source.

Let \(F_{34,N}\) be the literal message
\[
 F_{34,N}(w,Y)=N\operatorname{CT}_X
                [U_{0,N}(w,X)C_{1,N}(X,Y)].
\]
The complete next transfer is
\[
 \mathcal T_{10}F_{34,N}
 =N[Y^0](F_{34,N}d_NC_{0,N})
       +N[Y^N](F_{34,N}d_NC_{0,N}).
 \tag{3}
\]
Both terms in (3) are necessary: their original Laurent band is
\([-D,2D]\). Equivalently this is the full physical sum
\(\sum_bF_{34,N}(w,r^b)C_{0,N}(r^b,Z)/P_b\), where
\(P_b=(r;r)_b\). See
[the literal transfer, Section 1](research_mixed_literal_transfer_norm_obstruction.md)
and [the complete lower-half assembly](research_mixed_next_three_actual_complete_lower_left.md).

The [lowered-word identity, equations (5)--(6)](research_mixed_next_lowered_word_dual_observation.md)
gives, with \(\ell(w)=v(w)^TA_3^2\),
\[
 F_{34,N}(w,r^b)=\frac{(-q)^bP_b}{\kappa^2N}\ell_b(w).
 \tag{4}
\]
The full physical conditional matrix is exactly
\[
 K_{ab}=C_{0,N}(r^a,r^b),\qquad K=UHU^*,
 \tag{5}
\]
by [the actual Gram identity, equation (6)](research_mixed_next_actual_forcing_gram_bounds.md).
Since the outgoing polynomial has degree at most \(D\), its
entire physical column is \(K\mathfrak l(Z)\). Substitution
of (4)--(5) in the physical sum yields
\[
 \mathcal T_{10}F_{34,N}
       =\frac1{\kappa^2N}\ell(w)H g(Z).
 \tag{6}
\]
The exact original similarity
\(MA_3M^{-1}=\kappa H\) therefore proves
\[
 \boxed{\quad
 \mathcal T_{10}F_{34,N}(w,Z)
   =\frac1N v(w)^TM^{-1}\,T\,g(Z),
 \qquad T=H^2MH.
 \quad}
 \tag{7}
\]
In particular no factor \(N\), old factorial, or second sampled
coefficient has disappeared. These are identities of the full
outside polynomials, at both parities and with all original normal
directions. They also give the ordinary-word identity
\[
 A_3A_4A_3=\kappa^3M^{-1}TM,
 \tag{8}
\]
using \(MA_4M^{-1}=\kappa HM\). The right observation in
(7) is \(g(Z)\), whereas the ordinary right boundary in (8)
would be \(Mv(z)\).

## 2. Every rotation has an indefinite Hermitian part

Use the natural positive metric \(G=H^{-1}\), with
\(\langle x,y\rangle_G=x^*Gy\). Directly from (7),
\[
 \langle x,Tx\rangle_G=(Hx)^*M(Hx).
 \tag{9}
\]
Consequently the phase-rotated Hermitian quadratic form is
\[
 \operatorname{Re}\{e^{-i\theta}\langle x,Tx\rangle_G\}
   =x^*H\operatorname{Re}(e^{-i\theta}M)Hx.
 \tag{10}
\]
Since \(H\) is invertible, this is a Hermitian congruence.
Equivalently,
\[
 G^{1/2}TG^{-1/2}=H^{3/2}MH^{3/2}.
 \tag{11}
\]

**Proposition.** For every \(N>6\) and every real \(\theta\),
the quadratic form (10) takes both strictly positive and strictly
negative values. In particular the numerical range of \(T\) in
the metric \(G\) is contained in no rotated closed half-plane
whose boundary passes through zero.

The original triangular crossing formula in
[wire contraction, equation (6)](research_mixed_wire_exact_contraction.md)
has diagonal eigenvalues
\[
                  \lambda_j=\kappa(-1)^j q^{j(j+1)}.
 \tag{12}
\]
The first three are
\[
 \lambda_0=\kappa,\qquad
 \lambda_1=-\kappa e^{2\pi i/N},\qquad
 \lambda_2=\kappa e^{6\pi i/N}.
 \tag{13}
\]
After dividing by \(\kappa\), their circular order is
\(0,6\pi/N,\pi+2\pi/N\). The three consecutive angular
gaps are
\[
          6\pi/N,\qquad \pi-4\pi/N,\qquad \pi-2\pi/N.
 \tag{14}
\]
For \(N>6\), each belongs strictly to \((0,\pi)\).
Thus the three points are not contained in any closed semicircle.
For every \(\theta\), some \(\lambda_j\) in (13) has
\(\operatorname{Re}(e^{-i\theta}\lambda_j)>0\), and some
has strictly negative real part. This includes any rotation of
the original scalar \(\kappa^3\) in (8).

Every diagonal eigenvalue of a finite triangular matrix has a
nonzero right eigenvector, regardless of its other Jordan blocks.
If \(Mu_j=\lambda_ju_j\), then
\[
 u_j^*\operatorname{Re}(e^{-i\theta}M)u_j
       =\operatorname{Re}(e^{-i\theta}\lambda_j)\|u_j\|_2^2.
 \tag{15}
\]
The two signs just obtained prove indefiniteness. Taking
\(x_j=H^{-1}u_j\) in (10) proves the stated weighted version.
This proves the proposition without evaluating any finite matrix.

## 3. The source-specific gap remains

The complete physical matrix \(K\) in (5) is positive, but the
particular composition has the intervening crossing \(M\) in
(7). Equations (9)--(15) show why inserting the natural positive
metric does not turn that composition into a phase-definite
quadratic form. Moreover (7) is a bilinear observation with the
two distinct, fixed outside vectors; it is not itself (9).

This result does not assert cancellation of the actual transfer,
rule out a different metric on a source-restricted class, or
exclude a cone through which the actual incoming vector can be
transported with a controlled closing observation. Such a statement
would need a source-specific estimate beyond (7). The existing
ordinary \(33\) source theorem bounds its ordinary evaluation
kernel, while the exact lowered-word representation retains the
different inverse-crossing endpoint observation in its Section 6.
That observation has not been bounded here.

In particular the nonzero lower-half contribution in the actual
assembly remains valid, and its three signed complementary
integrals remain to be compared. No new full-transfer bound or
knot-family conclusion follows from this obstruction.
