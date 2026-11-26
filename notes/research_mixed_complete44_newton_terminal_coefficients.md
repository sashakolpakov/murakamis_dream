# Exact terminal values as the Newton coefficients of the complete \(44\) prefix

Private written deduction, 11 November 2026. The first physical sum
in a complete two-letter prefix is exactly a reversed terminal
observation. This gives its full Newton coefficients without taking
absolute values inside that observation. The result is an explicit
coefficient consequence of the existing reversed-cap identity,
not a new terminal-source estimate.

No mathematical numerical evaluation or change to a frozen source
is used.

## 1. Finite reciprocity and arbitrary input

Fix \(N\ge2\), and put
\[
 r=e^{-2\pi i/N},\quad D=N-1,\quad
 P_j=(r;r)_j,\quad p_j(X)=(rX;r)_j,\qquad 0\le j<N.
 \tag{1}
\]
All \(P_j\) in this note are nonzero. For any polynomial \(F\) of
degree at most \(D\), define
\[
 \mathscr V_{\alpha,N}[F](X)
 =\sum_{k=0}^{D}\frac{X^{-k}p_k(X)}{P_k^{1+\alpha}}F(r^k),
 \qquad \alpha\in\{0,1\}.
 \tag{2}
\]
This is the exact negative-band transform in
[reversed-cap assembly, equation (9)](research_mixed_reversed_cap_assembly.md)
and [forced terminal transport, equation (3)](research_mixed_terminal_gram_shift.md).
Its band is \([-D,0]\). The definition (2) makes sense for every
input \(F\); identifying it with an actual terminal cap will require
the original input in Section 2.

For \(0\le j,k<N\),
\[
 \boxed{\quad P_jp_k(r^j)=P_kp_j(r^k).\quad}
 \tag{3}
\]
If \(j+k<N\), both sides equal \(P_{j+k}\). If \(j+k\ge N\),
both sides vanish because the corresponding product contains
\(1-r^N\). Thus (3) uses no division by a vanishing Newton value
and includes both endpoint indices.

Keep the original conditional kernel and complete transfer
\[
 C_{\beta,N}(X,Y)=\sum_{j=0}^{D}
       \frac{X^{-j}p_j(X)p_j(Y)}{P_j^{2+\beta}},
 \qquad \beta\in\{0,1\},
 \tag{4}
\]
\[
 \mathsf T_{\alpha\beta,N}F
 =N\operatorname{CT}_X
 \!\left[F(X)\{d_N(X)(1+X^{-N})\}^{\alpha}
                          C_{\beta,N}(X,Y)\right]
 =\sum_{k=0}^{D}\frac{F(r^k)}{P_k^\alpha}
                          C_{\beta,N}(r^k,Y).
 \tag{5}
\]
The exact equality and its bands are
[literal transfer, Proposition 1](research_mixed_literal_transfer_norm_obstruction.md).
Here \(d_N\) is the original degree-\(D\) polynomial with
\(d_N(r^k)=P_k^{-1}\), including its finite forcing.

**Proposition 1.** Define the coherent coefficient
\[
 G_j^{(\alpha)}[F]
 =\sum_{k=0}^{D}
       \frac{F(r^k)r^{-kj}p_j(r^k)}{P_k^\alpha}.
 \tag{6}
\]
Then the following are exact identities:
\[
 \boxed{\quad
 G_j^{(\alpha)}[F]
       =P_j\mathscr V_{\alpha,N}[F](r^j),\qquad
 \mathsf T_{\alpha\beta,N}F(Y)
       =\sum_{j=0}^{D}
          \frac{\mathscr V_{\alpha,N}[F](r^j)p_j(Y)}
                         {P_j^{1+\beta}}.
 \quad}
 \tag{7}
\]

*Proof.* Multiply (2), evaluated at \(X=r^j\), by \(P_j\)
and apply (3) to each term. This gives (6) exactly. Expanding
the finite kernel in the right side of (5) gives
\(\sum_jG_j^{(\alpha)}[F]p_j(Y)/P_j^{2+\beta}\);
substitution proves the second identity. All sums are finite.
\(\square\)

The polynomials \(p_j\) have distinct degrees and nonzero leading
coefficients, so (7) identifies their actual Newton coefficients.
For \(\alpha=1\), it applies to the sum of the two original first
Fourier coefficients. It does not identify either coefficient
separately with a physical sum or introduce a factor of two.
The sole \(N\) in (5) is already accounted for by root averaging.

## 2. Original \(33,34,43,44\) inputs and the matrix observation

Let \(H_N(w,r^{-i})\) be the complete original endpoint polynomial,
and set
\[
 U_{\alpha,N}(w,X)
 =\sum_{i=0}^{D}
       \frac{H_N(w,r^{-i})p_i(X)}{P_i^{1+\alpha}},
 \qquad
 f_{(3+\alpha)(3+\beta),N}
       =\mathsf T_{\alpha\beta,N}U_{\alpha,N}.
 \tag{8}
\]
The original reversed terminal cap is
\(\mathcal V_{\alpha,N}(w,X)
 =\mathscr V_{\alpha,N}[U_{\alpha,N}(w,\cdot)](X)\).
Consequently
\[
 \boxed{\quad
 f_{(3+\alpha)(3+\beta),N}(w,Y)
   =\sum_{j=0}^{D}
          \frac{\mathcal V_{\alpha,N}(w,r^j)p_j(Y)}
                         {P_j^{1+\beta}}.
 \quad}
 \tag{9}
\]
In particular the coefficient asked for in the complete \(44\)
source is
\[
 \boxed{\quad
 G_j=\sum_{k=0}^{D}
     \frac{U_{1,N}(w,r^k)p_j(r^k)r^{-kj}}{P_k}
       =P_j\mathcal V_{1,N}(w,r^j),\qquad
 f_{44,N}(w,Y)=\sum_{j=0}^{D}
              \frac{\mathcal V_{1,N}(w,r^j)p_j(Y)}{P_j^2}.
 \quad}
 \tag{10}
\]
This preserves the whole coherent first sum in each coefficient.
At \(j=D\), the only nonzero summand in (6) has \(k=0\);
therefore \(G_D=N U_{1,N}(w,1)\) and
\(\mathcal V_{1,N}(w,r^D)=U_{1,N}(w,1)\), consistently with
(10). No separate endpoint correction is necessary.

For the original matrix identification, write
\[
 q=e^{\pi i/N},\quad \kappa=q^{D^2/2},\quad
 A_n=JM^n,\quad v(w)=(e_0(w),\ldots,e_D(w))^T.
\]
The \(e_j\) are the original ordinary Newton basis; \(J\) is
coefficient reversal and \(M\) is the original crossing matrix,
with its full Hermite normal data. The exact identity in
[forced terminal transport, equation (2)](research_mixed_terminal_gram_shift.md)
gives
\[
 G_j^{(\alpha)}[U_{\alpha,N}]
 =\frac{P_j(-q)^{-j}}{\kappa^{1+\alpha}N^\alpha}
                  (M^*M^{2+\alpha}v(w))_j.
 \tag{11}
\]
The star here is conjugate transpose. Equation (11) does not
turn the observed coordinate into a squared norm.

The underlying original braid relation
\(MJM=\kappa M^*\) yields
\[
                         MA_n=\kappa M^*M^{n-1}
 \tag{12}
\]
for every integer \(n\), since the original \(M\) is invertible.
That matrix relation retains arbitrary twist powers. The
factorial kernels and prepared caps (4), (8), however, have been
identified here with original tangle sources only for
\(\alpha,\beta\in\{0,1\}\), namely powers three and four.
Changing their factorial exponents is not an established
representation of an arbitrary additional twist.

Equations (7)--(11) hold at every level and both parities and
differentiate in \(w\). The ordinary color is never replaced by a
physical spectral value. The source normalization is also consistent
with the complete message bridge
\[
 \mathcal E_1 f_{44,N}
                  =\frac{v(w)^TA_4^2h}{\kappa^4N^2},
 \tag{13}
\]
where \(\mathcal E_1\) and \(h\) are exactly the Fourier transform
and cardinal vector of
[the message bridge, equations (3), (9)](research_mixed_conditional_fourier_message_bridge.md).
There is no alteration of the represented word in (10).

## 3. The shrinking physical second interval

For a physical second node \(Y=r^b\), put \(\ell=D-b\).
Both \(p_j(Y)\) and the incoming factor in \(C_{\beta,N}(Y,Z)\)
vanish for \(j>\ell\). In particular \(b/N\ge1/2\) gives
\(0\le\ell\le\lfloor N/2\rfloor-1\), including the even
half-level node.

Set
\[
 \nu_h=(-1)^h r^{-h(h+1)/2},\qquad
 P_{D-h}=\frac{N}{\nu_hP_h}.
 \tag{14}
\]
The latter identity follows from \(P_D=N\) by reversing its last
\(h\) factors; it is also the original complementary factorial
identity in
[the lowered-word observation, equation (14)](research_mixed_next_lowered_word_dual_observation.md).
Then (10) gives the exact triangular density
\[
 \boxed{\quad
 \frac{f_{44,N}(w,r^b)}{P_b}C_{\beta,N}(r^b,Z)
 =\frac1N\sum_{j,k=0}^{\ell}
   \frac{\nu_\ell^2}{\nu_{\ell-j}\nu_k}\,
   \frac{\mathcal V_{1,N}(w,r^j)P_\ell^3p_k(Z)}
        {P_{\ell-j}P_{\ell-k}P_j^2P_k^{2+\beta}} .
 \quad}
 \tag{15}
\]
Indeed
\[
 p_j(r^b)=\frac{\nu_\ell P_\ell}
                       {\nu_{\ell-j}P_{\ell-j}},\qquad
 C_{\beta,N}(r^b,Z)
 =P_\ell\sum_{k=0}^{\ell}
       \frac{\nu_k^{-1}p_k(Z)}
                         {P_{\ell-k}P_k^{2+\beta}},
 \tag{16}
\]
the second being the exact physical reflection in the same source,
equation (16). Inserting (16) and \(P_b^{-1}=\nu_\ell P_\ell/N\)
proves (15).

Thus the complete first coefficient at every retained \(j\)
can be estimated coherently as an actual terminal observation,
before estimating the remaining triangle. Multiplication by
the original outgoing modulus halfweight, if present, leaves
(15) unchanged as an identity before that multiplication.
Summing selected physical second nodes is an exact finite
decomposition of the combined next transfer; it is not an
identification with either separate second Fourier contour.

The equality supplies no new calibrated bound for
\(\mathcal V_{1,N}(w,r^j)\) throughout \(0\le j/N\le1/2\).
In particular a signed bound for \(f_{44,N}\) at the half-period
does not bound each term of (15). Existing terminal comparisons
must be used on their actual printed incoming domains and with
their original affine calibration. No positive pairing,
noncancellation, complete right-real second contribution or
whole second-period theorem follows from (15) alone.

## 4. Direct source bindings

The following directly used statements were read against the
original source definitions. Metadata hashes are recorded without
mathematical evaluation.

| Source and exact implication | SHA256 |
|---|---|
| [Literal transfer](research_mixed_literal_transfer_norm_obstruction.md), Section 1: complete coefficient/physical identity and two-sector normalization | `e9ce5a518439ed23b94c70eb548470ecbf9abfa5bd7c880f6828ed594a3fe0a3` |
| [Reversed-cap assembly](research_mixed_reversed_cap_assembly.md), Section 3: original negative-band terminal transform and full cap | `79d44dfbcfe8c598783f27a49dea5bc716cc62e0a2c4762a238f3b2afffd244c` |
| [Forced terminal transport](research_mixed_terminal_gram_shift.md), Sections 1–2: original matrix observation, braid relation and arbitrary-input transform | `f8e8cee9feaf1966fd2e1f85e30074856ded31d3a5e57ebdebb7affa9cf1fa90` |
| [Conditional/Fourier message bridge](research_mixed_conditional_fourier_message_bridge.md), Sections 1–2: exact original \(A_4^2\) normalization | `f09dd7a3b002481eba41fefccfe5bf25c3aed87e95673f60c75e2a81fbf06e50` |
| [Lowered-word observation](research_mixed_next_lowered_word_dual_observation.md), Section 2: complementary factorial and triangular physical kernel | `4ae7415fb46045c4e95b79361baece9f5922f046233a2b0d302a36c9a2d37d9d` |
