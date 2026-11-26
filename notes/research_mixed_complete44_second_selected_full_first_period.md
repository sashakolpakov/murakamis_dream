# The complete first period on the second selected plateau

Private written assembly, 11 November 2026. Both first Fourier
coefficients of the literal \(44\) prefix are now bounded after
attachment to the second selected weight and the third conditional
factor. Thus the complete polynomial \(f_{44}\), rather than one
first coefficient or a restricted first contour, may be used on
the entire selected second plateau. The subsequent second integral
in this note is still restricted to that plateau.

## 1. Exact finite source and common action

Fix an actual positive three/four word of length \(m\ge4\)
beginning with \(443\) or \(444\), with flags \((1,1,\beta)\),
\(\beta=0,1\), and original reference \(r_j\). Put
\[
 P=[11/50,9/20],\quad H=1/100,\quad c=\Im r_1<0,\quad
 y=b+iH,\quad z=v+i\Im r_3,\quad b,v\in P.
 \tag{1}
\]
The two conditional private indices are ordinary also at \(m=4\);
there the third outgoing incidence meets the original terminal
transform. The original following typed leg and all reference
correlations remain unchanged.

With \(q_N=e^{-2\pi i/N}\), \(P_j=(q_N;q_N)_j\),
\(p_j(X)=(q_NX;q_N)_j\), retain
\[
\begin{split}
 U_{1,N}(w,X)&=\sum_{i=0}^{N-1}
                    H_N(w,q_N^{-i})p_i(X)/P_i^2,\\
 C_{\epsilon,N}(X,Y)&=\sum_{j=0}^{N-1}
                    X^{-j}p_j(X)p_j(Y)/P_j^{2+\epsilon},\\
 L_N(w;X,Y)&=U_{1,N}(w,X)d_N(X)C_{1,N}(X,Y).
\end{split}
 \tag{2}
\]
Here \(H_N\) is complete and \(d_N(q_N^j)=P_j^{-1}\),
\(0\le j<N\), with \(\deg d_N<N\). All these \(P_j\) are
nonzero. Define the original two coefficient polynomials
\[
 f^{(0)}_{44,N}=N[X^0]L_N,\qquad
 f^{(1)}_{44,N}=N[X^N]L_N,\qquad
 f_{44,N}=f^{(0)}_{44,N}+f^{(1)}_{44,N}.
 \tag{3}
\]
The exact Laurent band of \(L_N\) is contained in
\([-N+1,2N-2]\): its cap and diagonal factors each have degree
at most \(N-1\), and every conditional row has \(X\)-exponents
between \(-j\) and zero. Only zero and \(N\) can be multiples
of \(N\) in this band. The original root filter therefore gives
\[
 f_{44,N}(w,Y)=
   \sum_{j=0}^{N-1}\frac{U_{1,N}(w,q_N^j)}{P_j}
                                      C_{1,N}(q_N^j,Y).
 \tag{4}
\]
This is the single unnormalized physical sum of the
[pointwise prefix theorem](research_mixed_four_four_pointwise_prefix_replacement.md),
equation (3). There is no additional factor two, \(1/N\),
\(\kappa_N\), or outgoing diagonal factor in (4). The degrees
in \(w,Y\) are at most \(N-1\).

Let \(g\), \(S\), all logarithmic lifts, and the three-factor
phase be those of the
[first-selected coefficient theorem](research_mixed_complete44_first_selected_coefficient.md):
\[
\begin{split}
 \Psi(e,a)&=S(e)+g(e+a)-g(a)-g(e)-\frac{\pi i}{2}(e-e^2),\\
 Q_\epsilon(s;a,b)&=g(s+a)+g(s+b)-(2+\epsilon)g(s)
                              -g(a)-g(b)+2\pi ias,\\
 F_{123}&=\Psi(e,z_1)+Q_1(s_2;z_1,z_2)
                 +Q_\beta(s_3;z_2,z_3)
                    -g(z_1)-g(z_2)-\frac\beta2g(z_3),\\
 p_R&=g'(s_3^*+r_3)-(1+\beta/2)g'(r_3),\\
 \Lambda_{123}(z)&=\Re F_{123,*}+\Re\{p_R(z-r_3)\}.
\end{split}
 \tag{5}
\]
The star denotes the unchanged critical reference of the actual
word. Every source used below has exactly (5), including its
absolute action and outgoing marginal.

Write \(Y=e^{-2\pi iy}\), \(Z=e^{-2\pi iz}\), and carry the
outgoing allocation
\[
 D_{\beta,N}(Z)=
 \begin{cases}1,&\beta=0,\\ |d_N(Z)|^{1/2},&\beta=1.\end{cases}
 \tag{6}
\]
It is a modulus multiplier, not a holomorphic square root.
At its zeros it will not be divided out.

## 2. The complementary first coefficient on its full negative path

For \(X(a)=e^{-2\pi ia}\), the finite coefficient identity is
\[
 f^{(0)}_{44,N}(w,Y)
       =N\int_0^1 L_N(w;X(a),Y)\,da.
 \tag{7}
\]
Because this is a finite Laurent polynomial in a nonvanishing
exponential, the integrand is entire in the additive variable
\(a\). Cauchy's theorem replaces the real interval exactly by
\[
\begin{split}
 {\cal H}_0:\quad
 0&\longrightarrow1/10
  \longrightarrow1/10+ic
  \longrightarrow9/20+ic\\
  &\longrightarrow1/2+ic
  \longrightarrow1/2
  \longrightarrow7/8
  \longrightarrow1 .
\end{split}
 \tag{8}
\]
The path and its heights are fixed independently of \(N,w,y,z\).
Negative powers of \(X\) create no finite singularity in \(a\).
No physical-node substitution is made during this deformation.

Multiply the exact identity (7) by
\(d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)\) before taking moduli. Its
dependence on \(a\) is constant, so the result is bounded by
\[
 N\int_{{\cal H}_0}
 |U_{1,N}(w,X)C_{1,N}(X,Y)C_{\beta,N}(Y,Z)
                 d_N(X)d_N(Y)Y^{-N}|\,
                          D_{\beta,N}(Z)\,|da|.
 \tag{9}
\]
The entire finite product in (9) has the following adopted bounds:

| Portion of \({\cal H}_0\) | Gap below \(\Lambda_{123}\) | Source |
|---|---:|---|
| \(0\to1/10\) | \(1/400\) | [Selected-left connection](research_mixed_complete44_second_selected_first_left_connection.md), Theorem (39), whose real segment permits either first monomial |
| \(1/10\to1/10+ic\to9/20+ic\) | \(1/6400\) | [Negative-left connection](research_mixed_complete44_second_selected_negative_left_connection.md), Theorem (32) |
| \(9/20+ic\to1/2+ic\to1/2\) | \(1/12800\) | [Right-half connections](research_mixed_complete44_second_selected_right_half_connections.md), Theorem 1, first unselected case |
| \([1/2,7/8]\) | \(1/12800\) | [Real first arc](research_mixed_complete44_second_selected_real_first_arc.md), Theorem (34), first unselected case |
| \([7/8,1]\) | \(1/200\) | [Near-one first arc](research_mixed_complete44_second_selected_far_first_arc.md), Theorem (31), first unselected case |

Each entry bounds the literal complete three-factor product, with
the whole first weight, the whole selected second weight, both of
their upper-rate alternatives and (6). All internal cap and
conditional rows, joins, aliases and true endpoint groups were
already retained in those proofs. In particular the closed endpoint
one belongs to the last entry; no unproved uniform passage to that
endpoint is needed here.

Set \(\delta=1/12800\). Choose each source tolerance below a
prescribed \(\tau>0\), reducing it further when needed for a
common ordinary-color disk. The path has fixed finite length.
Its original density is exactly \(+N\,da\), and this factor
and all path lengths are absorbed into a polynomial prefactor.
Thus, at both parities,
\[
\begin{split}
 &|f^{(0)}_{44,N}(w,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
                                      D_{\beta,N}(Z)\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
                 e^{N\{\Lambda_{123}(z)-\delta+\tau\}} .
\end{split}
 \tag{10}
\]
The estimate holds for all real \(w\in[-2,2]\), then on a
sufficiently small fixed ordinary-color disk, with every fixed
derivative on smaller disks. These scopes come from the five
uniform source bounds. Alternatively their common degree bound
continues the all-real estimate with arbitrarily small rate cost;
the color-independent factors in (9) remain multipliers throughout.

## 3. The whole \(44\) polynomial and its second selected interval

The first-selected coefficient theorem already proves (10) with
\(f^{(0)}_{44,N}\) replaced by \(f^{(1)}_{44,N}\), at the
same \(\delta\), action, targets, colors and parities. Its first
path uses height \(H\), but its coefficient and source retain the
first selected monomial exactly. Adding the two estimates and
using the exact identity (3) gives the following conclusion.

**Theorem.** On (1), for every \(\tau>0\),
\[
\begin{split}
 &|f_{44,N}(w,Y)d_N(Y)Y^{-N}C_{\beta,N}(Y,Z)|
                                      D_{\beta,N}(Z)\\
 &\hspace{12mm}\le C_\tau N^{A_\tau}
                 e^{N\{\Lambda_{123}(z)-1/12800+\tau\}}.
\end{split}
 \tag{11}
\]
It holds at both level parities, uniformly in \(b,v\in P\)
and every real ordinary color \(w\in[-2,2]\), and on a
sufficiently small fixed ordinary-color disk about \(-2\).
Every fixed ordinary-color derivative has the same rate on
smaller disks, with a polynomial prefactor. The triangle inequality
adds only a constant factor; it neither alters the physical sum
(4) nor asserts positivity of its summands.

Define the exact subsequent selected-interval polynomial
\[
 {\cal E}_{1,\beta,N}(w,Z)=
  N\int_{P+iH}f_{44,N}(w,e^{-2\pi iy})\,
       d_N(e^{-2\pi iy})e^{2\pi iNy}
                         C_{\beta,N}(e^{-2\pi iy},Z)\,dy .
 \tag{12}
\]
The orientation is increasing real part. The interval and its
height are fixed, and its original density is \(N\,dy\).
Uniformity in \(y\) in (11) therefore gives
\[
 |{\cal E}_{1,\beta,N}(w,Z)|D_{\beta,N}(Z)
 \le C_\tau N^{A_\tau}
                   e^{N\{\Lambda_{123}(z)-1/12800+\tau\}},
 \tag{13}
\]
with the same color and parity scopes. Expanding \(f_{44}\)
as its two exact first integrals gives precisely the original
two densities \(N^2\,da\,dy\). The first complete weight has
been consumed once in (3)--(4); the second whole weight and
its selected monomial occur once in (12). The third outgoing
halfweight is carried once in (13), leaving its other incidence
to the next original factor, or the terminal factor at \(m=4\).
No exterior unit scalar or further power of \(N\) is inserted.

The first period in (11)--(13) is complete: it is the full
physical polynomial (4). The second coordinate is still restricted
to \(P+iH\). Its unselected complement, selected complementary
arcs and joins, and a bound for the complete next transfer remain
separate. These estimates do not give a full second-period
asymptotic, a nonzero coefficient for that whole transfer, or a
whole-word or knot theorem.

## Direct source versions

| Source | SHA-256 |
|---|---|
| research_mixed_complete44_first_selected_coefficient.md | f63fb40f521b6b2f82e0cde84223ba5e4f8af93d3240ab261b7527cc97a0afcf |
| research_mixed_complete44_second_selected_negative_left_connection.md | 878cbd67c6035f6fb9903e76d0b719cae599874d852710d979282e711d7fbf77 |
| research_mixed_complete44_second_selected_first_left_connection.md | f91bbac2d0843fec8fd5e9ddc29b4d35efbbdf708f2e5bd8d4db6c686b58c702 |
| research_mixed_complete44_second_selected_right_half_connections.md | 49358cc1d991a59a8fbf38c64306e9d88e64b127e2e8a5229d741972036d00d5 |
| research_mixed_complete44_second_selected_real_first_arc.md | f9a9a53a68faf11293f8463e713afdb951ffd5cddcf18e8f1dee4d09ff5fb37c |
| research_mixed_complete44_second_selected_far_first_arc.md | f163f164be985de37d8d10485ec0790fe5057496d94030afdf5c7b48658cc8be |
| research_mixed_four_four_pointwise_prefix_replacement.md | 2a4a86ced4bb326baa2ca24bfd6f9c6846103070f4a0731f663ef6d2303a89b7 |

The complete written proof and all seven direct source implications
were read, with matching bindings. No mathematical numerical
evaluation, saved-value arithmetic, import, test, compilation or
frozen-source edit is used. Independent proof and direct-source
review is required before adoption.
