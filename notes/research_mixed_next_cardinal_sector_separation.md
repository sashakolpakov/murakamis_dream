# Exact sector separation for a cardinal-filtered next source

Research deduction, 7 November 2026. A physical-index deletion in the
next three/four transfer controls the sum of its two Fourier sectors.
The individual sectors have an exact additional term: a divided
difference of the original reciprocal-factorial polynomial. This note
identifies that term, its full sampled derivative, and the original
finite row support. No source evaluation is used.

Polynomial division by \(Y^N-1\) is elementary and is not a new
asymptotic theorem. The useful specialization below is the exact
cardinal correction, including its diagonal derivative and every
off-diagonal physical index. In particular the additional term is not
replaced by a value of a reciprocal factorial.

## 1. The exact two-sector functional

Put
\[
 D=N-1,\quad r=e^{-2\pi i/N},\quad B_b=r^b,\quad
 P_b=(r;r)_b,\quad d_b=P_b^{-1}.
 \tag{1}
\]
The polynomial \(d=d_N\) has degree at most \(D\) and satisfies
\(d(B_b)=d_b\). Let
\[
 C(Y,Z)=C_{\beta,N}(Y,Z)
   =\sum_{j=0}^{D}
      \frac{Y^{-j}p_j(Y)p_j(Z)}{P_j^{2+\beta}},
 \qquad p_j(Y)=(rY;r)_j,\quad\beta=0,1.
 \tag{2}
\]
Its \(Y\)-frequencies lie in \([-D,0]\). For any polynomial
\(E(Y)\) of degree at most \(D\), define
\[
 S_0[E]=N[Y^0](EdC),\qquad S_1[E]=N[Y^N](EdC).
 \tag{3}
\]
The [original next-attachment identity](research_mixed_three_four_next_conditional_attachment.md)
gives exactly
\[
 S_0[E]+S_1[E]
       =\sum_{b=0}^{D}E(B_b)d_bC(B_b,Z).
 \tag{4}
\]
Indeed \(EdC\) has band \([-D,2D]\), whose only multiples of
\(N\) are \(0,N\). There is no extra Gram matrix or scalar in
(3)--(4). The original outgoing ordinary observation, if subsequently
applied, retains the separate scalar in that attachment identity.

## 2. Each cardinal node has one explicit correction

Use the original cardinal polynomials
\[
 \mathfrak l_b(Y)=\frac1N\sum_{\nu=0}^{D}(Yr^{-b})^\nu
     =\frac{B_b}{N}\frac{Y^N-1}{Y-B_b}.
 \tag{5}
\]
For every \(b\), set
\[
 Q_b(Y)=\frac{B_b}{N}
                  \frac{d(Y)-d_b}{Y-B_b}.
 \tag{6}
\]
The apparent singularity is removable, and \(\deg Q_b\le N-2\).
Multiplication in (5) gives the polynomial identity
\[
 \mathfrak l_b(Y)d(Y)
       =d_b\mathfrak l_b(Y)+(Y^N-1)Q_b(Y).
 \tag{7}
\]
Since \(\mathfrak l_bC\) has band \([-D,D]\), its coefficient
of degree \(N\) vanishes. Since \(Q_bC\) has band
\([-D,D-1]\), its coefficient of degree \(N\) also vanishes.
Therefore
\[
 \boxed{\begin{split}
 S_1[\mathfrak l_b]&=N\operatorname{CT}_Y[Q_b(Y)C(Y,Z)],\\
 S_0[\mathfrak l_b]&=d_bC(B_b,Z)
                          -N\operatorname{CT}_Y[Q_b(Y)C(Y,Z)].
 \end{split}}                                                    \tag{8}
\]
Both copies of the correction have their displayed signs.

For a set \(I\subset\{0,\ldots,D\}\), the exact cardinal removal
of a prefix \(F\) is \(E_I=\sum_{b\in I}F(B_b)\mathfrak l_b\).
Thus its two corrections are obtained from (8) by summing against
the actual coefficients \(F(B_b)\). No partial root sum is replaced
by an arc. In particular for the original prefix,
\[
 F_{34,N}(w,B_b)
     =\frac{(-q)^bP_b}{\kappa^2N}\ell_{b,N}(w)
 \tag{9}
\]
by [the lowered-word identity](research_mixed_next_lowered_word_dual_observation.md).
Equation (9) cancels \(P_b\) in the first term of (8), but it
does not remove \(Q_b\) from the second term.

For a general \(E\), put
\[
 I_N(Ed)=\sum_bE(B_b)d_b\mathfrak l_b,\qquad
 Q_E=\sum_bE(B_b)Q_b .
 \tag{10}
\]
Then exactly
\[
 Ed=I_N(Ed)+(Y^N-1)Q_E,\qquad
 S_1[E]=N\operatorname{CT}(Q_EC).
 \tag{11}
\]
Equivalently \(Q_E\) is the polynomial formed from the coefficients
of \(Ed\) of degrees at least \(N\), shifted down by \(N\).
Its degree is at most \(\deg E-1\), with \(Q_E=0\) when \(E\)
is constant. Thus a constant prefix has no second sector, and
\(\sum_bQ_b=0\) exactly. A cardinal projection of that constant
need not retain this cancellation.

## 3. Full physical derivatives and the discrete product defect

Let \(\mathsf D\) be the exact matrix for \(Y\partial_Y\) on
degree-\(D\) cardinal polynomials, evaluated on the root grid.
Direct differentiation of (5) gives
\[
 \mathsf D_{ab}=
 \begin{cases}
 B_b/(B_a-B_b),&a\ne b,\\
 D/2,&a=b.
 \end{cases}
 \tag{12}
\]
Consequently the correction in (6) has the full sampled formula
\[
 Q_b(B_a)=
 \begin{cases}
 N^{-1}(d_a-d_b)\mathsf D_{ab},&a\ne b,\\
 N^{-1}B_b d'(B_b),&a=b.
 \end{cases}
 \tag{13}
\]
The band of \(Q_bC\) contains no nonzero multiple of \(N\).
Thus (8) can also be written
\[
 S_1[\mathfrak l_b]=\sum_{a=0}^{D}Q_b(B_a)C(B_a,Z).
 \tag{14}
\]
Every index \(a\) in (14) remains, even when \(b\) is an end
index. The derivative on its diagonal is part of the polynomial
identity, not a value-only substitution.

Write \(e_a=E(B_a)\), and let products of sampled vectors denote
pointwise products. Differentiating (11) at \(Y=B_a\) proves
\[
 \boxed{\quad
 Q_E(B_a)=\frac1N
       \{d_a(\mathsf De)_a+e_a(\mathsf Dd)_a
                                      -(\mathsf D(ed))_a\}.
 \quad}                                                         \tag{15}
\]
This is an exact product-rule defect: \(\mathsf D(ed)\) differentiates
the degree-\(D\) interpolant of the product values, rather than the
unreduced product \(Ed\).

There is an equivalent derivative formula without cardinal notation:
\[
 \boxed{\quad
 S_1[E]=\frac1N\sum_{a=0}^{D}
        \left[Y\partial_Y\{E(Y)d(Y)C(Y,Z)\}\right]_{Y=B_a}.
 \quad}                                                         \tag{16}
\]
To prove it, apply the root sum to each frequency of \(EdC\).
The zero frequency has derivative zero; the frequency \(N\)
has derivative multiplier \(N\); the root sum supplies a further
factor \(N\). Dividing by \(N\) leaves precisely (3).
There are no other resonant frequencies in its exact band.

The entries in (12) are polynomially bounded in \(N\):
\[
 |\mathsf D_{ab}|
   =\frac1{2|\sin(\pi(a-b)/N)|}\le\frac N4\quad(a\ne b),
 \qquad |\mathsf D_{aa}|\le N/2.
 \tag{17}
\]
Here \(\sin(\pi/N)\ge2/N\). This does not bound (15) by only
the diagonal products \(|e_ad_aC(B_a,Z)|\): the terms with
\(a\ne b\) in (13)--(14) pair different original indices.
It identifies exactly what additional sampled derivative or
cross-index estimate a polynomial-loss upgrade would have to use.

## 4. The original forced moments remain explicit

Write \(d(Y)=\sum_{k=0}^{D}\widehat d_kY^k\), distinguishing
these coefficients from the sampled values \(d_b\) in (1).
The original forced equation
in [Fourier-weight continuation, equation (5)](research_mixed_fourier_weight_continuation.md)
gives
\[
 \widehat d_D=\frac1{N^2},\qquad
 \widehat d_{k-1}=(1-r^{-k})\widehat d_k+\frac1{N^2}
                                      \quad(1\le k\le D).
 \tag{18}
\]
Backward induction therefore yields
\[
 \widehat d_{D-j}=\frac{P_j}{N^2}\sum_{h=0}^{j}\frac1{P_h},
                    \qquad0\le j\le D .
 \tag{19}
\]
All denominators are below \(N\), hence nonzero. Substitution
in (6) gives the finite polynomial
\[
 Q_b(Y)=\frac1N\sum_{k=1}^{D}\widehat d_k
                    \sum_{j=0}^{k-1}B_b^{\,k-j}Y^j .
 \tag{20}
\]
For \(b=0\), in particular,
\[
 S_1[\mathfrak l_0]
    =\operatorname{CT}_Y
          \left[\frac{d(Y)-1}{Y-1}C(Y,Z)\right].
 \tag{21}
\]
On a circle \(|Y|>1\), the term \(-C(Y,Z)/(Y-1)\) has
only strictly negative powers and has zero constant coefficient.
Thus \(d(Y)/(Y-1)\) may replace the quotient in (21) on that
circle, but its full positive-frequency part remains. Equation
(19) does not discard its partial reciprocal-factorial sums.

All statements are finite polynomial or Laurent-polynomial
identities at every \(N\ge2\), both parities, every ordinary color,
and every complex output. They may be differentiated in the actual
outside variables before or after the displayed finite operations.
The original Hermite data enter through the exact source (9);
none of its matrices or normals has been replaced.

These identities keep the complete two-sector correction to the
low/high cardinal filters used in
[the physical middle-rectangle theorem](research_mixed_next_low_physical_interval.md).
The proved combined physical deletion and the local packet preserved
by that filter remain valid. Separate suppression of either sector
requires an estimate of (11), (14), or (16); cancellation of the
two copies in (8) alone proves only their combined bound.
