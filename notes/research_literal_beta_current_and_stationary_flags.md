# The literal beta elimination with its endpoint current and stationary flags

Private written proof, 17 November 2026. The three beta convolutions
in the proved nine-cell evaluation [C] admit an exact polynomial
source transport, including the cyclic seam and every Fourier normal.
Their regular classical characteristic is a specified five-flag
relation. This does not identify a relative geometric integration
cycle or its coefficient.

## 1. The actual finite transform

Use the roots and normalizations of [C,B,S]. Let \(N>2\) be odd,
\(d=N-1\), and \(q=\exp(2\pi i/N)\). For five ordered labels put

\[
 A=abcd,\quad B=abce,\quad C=acde,\quad D=bcde,\quad E=abde.
\]

The letters here label tetrahedra. Their nonzero root parameters
obey \(\alpha_T^N+\beta_T^N=1\). Fix \(L\in\mathbb Z/N\), and set

\[
 x=\alpha_A,\quad b=\alpha_Bq^L,\quad
 z=\beta_A/\beta_B=\alpha_D,\quad
 g_r=\frac{W_A(r)}{\overline W_B(r+L)}.
 \tag{1}
\]

All \(g_r\) are nonzero, periodic, and satisfy the literal recurrence

\[
 \frac{g_{r+1}}{g_r}
       =z\frac{1-bq^r}{1-xq^{r+1}},\qquad g_N=g_0.
 \tag{2}
\]

Write \(S e_r=e_{r+1}\), \(Z e_r=q^r e_r\), and
\(F_{Kr}=q^{Kr}\). The invertible finite beta transform is

\[
 B_L=F\operatorname{diag}(g_r),\qquad
 B_L^{-1}=\operatorname{diag}(g_r^{-1})F^{-1}.
 \tag{3}
\]

Its unit column is exactly the proved convolution [C,(9)]:

\[
 (B_L\mathbf1)_K
 =\mathfrak f_{abcde}
   \frac{\overline W_C(K+L)}
        {\overline W_D(K)\overline W_E(L)}.
 \tag{4}
\]

In particular the finite scalar \(\mathfrak f\) is retained. Formula
(4) evaluates the unit input; arbitrary attachments use (3).

Conjugation gives, with the displayed order of factors,

\[
 B_L ZB_L^{-1}=S^{-1},\qquad
 A_L:=B_LSB_L^{-1}
       =zZ(1-bS^{-1})(1-xqS^{-1})^{-1}.
 \tag{5}
\]

Indeed \(D_gSD_g^{-1}=S\operatorname{diag}(g_{r+1}/g_r)\),
while \(FSF^{-1}=Z\) and \(FZF^{-1}=S^{-1}\).
Let \(E_{ab}=|a\rangle\langle b|\). Direct Fourier inversion gives

\[
 (B_LE_{ab}B_L^{-1})_{KK'}
    =\frac{g_a}{Ng_b}q^{Ka-K'b},\qquad
 B_LE_{00}B_L^{-1}=P:=\frac1N\mathbf1\mathbf1^t.
 \tag{6}
\]

Consequently the original truncated raising shift
\(J_+=(I-E_{00})S\), which deletes \(d\to0\), becomes

\[
                    B_LJ_+B_L^{-1}=(I-P)A_L.          \tag{7}
\]

Thus the seam projector is not removed by the convolution.
For the actual integer number operator \(n e_r=r e_r\),

\[
 H:=B_LnB_L^{-1}=F nF^{-1},\qquad
 H_{KK}=d/2,\quad
 H_{KK'}=-\frac1{1-q^{K-K'}}\quad(K\ne K').           \tag{8}
\]

The off-diagonal formula follows by differentiating the finite
geometric sum at a nontrivial \(N\)-th root. Thus every finite
polynomial index moment has an explicit image, without discarding
an endpoint or selecting a different row.

## 2. The polynomial lift and all Fourier normals

Let \(\mathcal P_d\) be the polynomials in \(k\) of degree at most
\(d\). The specified, invertible lift of (3) is

\[
 \widehat B_L f(k)=\sum_{r=0}^{d}g_rf_rk^r.
 \tag{9}
\]

It samples to (3) at \(k=q^K\). On \(\mathcal P_d\) put

\[
 (\mathcal T G)(k)=G(qk),\quad
 \mathcal R=z(1-b\mathcal T)(1-xq\mathcal T)^{-1},\quad
 \chi(G)=\frac{g_0}{g_d}[k^d]G.
 \tag{10}
\]

The inverse in (10) exists: its eigenvalues are
\(1-xq^{r+1}\ne0\). Coefficient comparison, including \(r=d\),
proves the exact identities

\[
 \widehat B_LS\widehat B_L^{-1}G
       =k\mathcal R G+\chi(G)(1-k^N),
 \tag{11}
\]
\[
 \widehat B_LJ_+\widehat B_L^{-1}G
       =k\mathcal R G-\chi(G)k^N.                    \tag{12}
\]

In (11) the unwanted \(k^N\) coefficient cancels because the last
eigenvalue of \(\mathcal R\) is \(g_0/g_d\); the constant term is
the wrapped input. In (12) that input is deleted. These are identities
in ordinary polynomials, not only modulo \(k^N-1\).
The image of \(E_{00}\) under (9) is \(G\mapsto[k^0]G\).

Apply (11) to \(G_L=\widehat B_L\mathbf1\), for which
\(S\mathbf1=\mathbf1\) and \(\chi(G_L)=g_0\). Multiplying by
\(1-x\mathcal T\), and using \(\mathcal T k=qk\mathcal T\), gives

\[
 \boxed{(1-kz)G_L(k)-(x-kzb)G_L(qk)
                   =(1-x)g_0(1-k^N).}              \tag{13}
\]

This also follows by summing (2) directly. The endpoint is not an
unspecified correction: \(g_0=\overline W_B(L)^{-1}\ne0\).
For the entire Fourier variable \(K\in\mathbb C\), substitute
\(k=\exp(2\pi iK/N)\). At every integer \(K\), the right side
vanishes, whereas its \(h\)-th \(K\)-derivative is exactly

\[
          -(2\pi i)^h(1-x)g_0\qquad(h\ge1).          \tag{14}
\]

For an arbitrary input \(G\), the omitted term in (11) has the same
derivatives with \((1-x)g_0\) replaced by \(\chi(G)\).
All derivatives are those of the specified polynomial (9); no
ordinary module of nonintegral color is introduced. Decoration
derivatives also retain (9)--(13), including derivatives of the
displayed coefficients. A different continuation in the discrete
parameter \(L\) is not asserted by these formulas.

There are useful uniform finite-operator bounds. On compact regular
central-parameter sets, all root choices and all \(L\) satisfy

\[
       \|A_L\|_2+\|A_L^{-1}\|_2\le C N,
       \qquad \|P\|_2=1,\qquad \|H\|_2=d.           \tag{15}
\]

To prove the first assertion, if \(u^N=U\ne1\), then
\((1-uq^r)\sum_{j<N}(uq^r)^j=1-U\) implies

\[
 |1-uq^r|\ge\frac{|1-U|}{N\max(1,|U|)}.
\]

Use this for the two denominators in (2) and its reciprocal.
The normalized Fourier matrix is unitary, so the two norms are
the maximum moduli of the cyclic ratios and their reciprocals.
Equation (8) proves the remaining statements. Hence fixed-length
words in these transported shifts, number operators and endpoint
projectors cost at most a power of \(N\). Moreover
\(\chi=z(1-b/q)(1-x)^{-1}[k^d]\). On unnormalized sample
\(\ell^2\), coefficient extraction has norm \(N^{-1/2}\), so
\(\|\chi\|\le C\sqrt N\). Thus every fixed Fourier normal of
the seam in (11) has polynomial norm, uniformly in \(L\).
This is not a bound on the condition number of \(B_L\), or on
every transported matrix unit.

## 3. Fixed-log normalization and the classical characteristic

For this section choose a compact lifted regular configuration
domain, with a slightly larger regular neighborhood, and fixed
bounded logarithms \(\ell_{ij}\) of \(z_i-z_j\), \(i<j\). At each
level take exactly \(s_{ij}=\exp(\ell_{ij}/N)\). Then every sorted
root ratio in [C,B] is \(\exp(u/N)\) for a bounded fixed logarithm
\(u\). Central degeneracies are excluded on the neighborhood.
These paths are not arbitrary level-dependent deck choices, and
need not be the real odd-root paths in [C,(6)].

On these domains the literal three beta scalars, all nine
\(\rho_T,\bar\rho_T\), and the exact \(C_N\) of [C,(4)] obey

\[
             N^{-M}\le |a_N|\le N^M                 \tag{16}
\]

for one domain-dependent \(M\), enlarged to cover the finite list.
Here and below fixed powers of \(N\) can absorb fixed constants.

Here is a direct proof, including the lower bound. For bounded \(u,v\)
with \(e^u,e^v\ne1\), uniformly in \(0\le r<N\),

\[
 N^{-M_0}\le\left|
 \prod_{j=1}^{r}\frac{1-e^{v/N}q^j}{1-e^{u/N}q^j}
                 \right|\le N^{M_0}.              \tag{17}
\]

For indices away from a fixed number at either endpoint, compare
each factor with \(1-q^j\). Its relative change is
\(O(1/\min(j,N-j))\), whose sum is \(O(\log N)\).
At the finitely many remaining indices, the limiting ratios are
nonzero ratios of \(u+2\pi ij\), \(v+2\pi ij\), or their versions
with \(j<0\). Compactness and \(e^u,e^v\ne1\) bound them above and
below. This proves (17). Each finite \(f\)-summand has polynomial
size, since its additional factor \(\exp(wr/N)\) is bounded.
Thus \(f\) and its paired sum in [B,(11)] have polynomial upper bounds.

For the beta parameters, that proved product simplifies exactly to

\[
 \mathfrak f_{abcde}
 f(\alpha_B,\alpha_A/q\mid\alpha_D^{-1})
 =N\frac{(1-\alpha_A)(1-\alpha_B)(1-\alpha_C)\beta_D^N}
          {\beta_A^N(1-\alpha_D)(1-\alpha_E)}.       \tag{18}
\]

Every \(1-\alpha_T\) is \(N^{-1}\) times a uniformly nonzero
bounded factor: its fixed logarithm cannot vanish because
\(\alpha_T^N\ne1\). Thus (18) is bounded above and below by positive
constants. The paired upper bound gives the required lower bound.
For the tetrahedral scalars, the brackets in [B,(2)] are bounded
units on these paths, and their finite sums have the same upper
bound. The exact identity [B,(12)]

\[
 \rho_T\bar\rho_T=Y_T^N/[N(Z_T-X_T)]
\]

is likewise a bounded unit, and proves both lower bounds.
Finally every root monomial to power \(d\) is bounded above and
below, and the remaining factors in [C,(4)] are explicit powers
of \(N\) times bounded units. This proves (16) for \(C_N\).
Buffered Cauchy estimates give polynomial bounds for every fixed
decoration derivative of these factors and their inverses.
In particular their logarithmic modulus divided by \(N\) tends to
zero uniformly. No constancy of their retained phase is claimed.

Now use \(k,l\in\mathbb C^*\), with \(k,l,kl\ne1\), as the
classical variables corresponding to \(q^K,q^L\). On the finite
grid the actual summand of (4) has the following ratio, which
is also a specified rational expression in those variables:

\[
       kz\frac{1-\alpha_Blt}{1-q\alpha_At},\qquad t=q^r.
 \tag{19}
\]

On the specified fixed-log paths its limiting logarithm has the
primitive

\[
 \Phi(R;K_0,L_0)=K_0R+\operatorname{Li}_2(e^R)
                            -\operatorname{Li}_2(e^{R+L_0}),
 \quad k=e^{K_0},\ l=e^{L_0},\ t=e^R.               \tag{20}
\]

This is the classical phase determined by the actual logarithmic
ratio. It does not prescribe a complex interpolation of the finite
products or an integration chain. On its regular logarithmic
stationary lift the ratio-one equation gives uniquely

\[
 t_*=\frac{1-k}{1-kl},\quad
 1-t_*=\frac{k(1-l)}{1-kl},\quad
 1-lt_* =\frac{1-l}{1-kl},\qquad
 \Phi_{RR}(t_*)=\frac{(1-k)(1-kl)}{k(1-l)}\ne0.
 \tag{21}
\]

Choose principal branches initially at \(0<k,l<1\), and then
continue every logarithm and dilogarithm along the same path in
the displayed regular domain. Differentiating in \(K_0,L_0\),
and fixing the constant by \(k\to0\) in that initial chamber, proves

\[
 \boxed{\Phi(t_*)=\operatorname{Li}_2(kl)
       -\operatorname{Li}_2(k)-\operatorname{Li}_2(l)
       +\operatorname{Li}_2(1).}                   \tag{22}
\]

Both sides are continued, not independently reset to principal
values. A logarithmic alias changes the lifted stationary equation
and its Fourier linear term; (22) does not erase those marks.
The three excluded divisors are explicit: \(k=1\) sends \(t_*\)
to zero, \(kl=1\) sends it to infinity, and \(l=1\) sends it to
the cyclic product seam \(t_*=1\).

There is a literal local flag certificate. For the five distinct
points \(p=(\infty,0,1,k,kl)\), use
\(\operatorname{cr}(a,b,c,d)=(p_a-p_d)(p_b-p_c)/
((p_a-p_c)(p_b-p_d))\). The five faces of this ordered four-simplex,
in omitted-vertex order, have ratios

\[
                 (lt_*,\ t_*,\ 1/l,\ 1/(kl),\ 1/k).
 \tag{23}
\]

This is checked directly, including the entries at infinity.
The alternating boundary is
\([lt_*]-[t_*]+[1/l]-[1/(kl)]+[1/k]\).
Swapping the last two vertices of a tetrahedron inverts its ratio
and reverses its orientation. With these literal reorderings this
is the negative of \([t_*]-[lt_*]-[kl]+[k]+[l]\), the five-term
characteristic in (22). The continued primitive (22), rather than
an unmarked symbol alone, specifies the logarithmic lift.
All the ratios are invariant under a common projective change of
the five flags. The flags in (23) are stationary index data, not
the six auxiliary vertex decorations of [S].

## 4. Application to the three actual eliminations and scope

The eliminations in [C, Section 3] use exactly the following rows:

\[
\begin{array}{c|c|c|c}
\text{summed index}&abcde&K&L\\ \hline
r&01235&u+v+1&1-k_1+s+z\\
s&01345&v+t+1+\ell&z+1-k_1\\
u&12345&t+1+\ell&v+1
\end{array}                                                     \tag{24}
\]

Here \(\ell\) is the finite degree introduced by the exact expansion
[C,(13)]; all other letters have the meanings in [C,S]. Apply
(3),(9)--(14) separately for every retained assignment of the
other finite indices. Keep \(K\) temporarily as an independent
output coordinate, then apply the literal evaluation row imposing
its affine value in (24). Likewise retain \(L\)'s dependence on
the remaining indices. For example the first row evaluates at
\(K=u+v+1\); a transformed shift must also act on that evaluation
row and every affected attachment. It must not act only on the
bare product (4) after this identification. Tensoring (3) with
the untouched finite indices and retaining these evaluation rows
is an exact identity for arbitrary attachments.
This is an actual source map for each
elimination, with arbitrary inserted arrays, all finite index
moments, and the specified Fourier normals. It keeps the scalar
(4), every carry in (24), and each endpoint functional \(\chi\).
It does not replace the remaining coefficient extractions in [C]
by saddles or suppress their support boundaries.

Thus the regular classical characteristic of each beta move has
the explicit local marked primitive (22) and five-flag boundary
(23), while the finite source has the nonzero endpoint current
(13). Their conjunction is more information than an unmarked
Bloch equality. It still does not establish that these local flags
assemble into a peripheral-relative \(\rho\)-equivariant development,
or that an original relative contour maps to a positive geometric
contour with nonzero coefficient. In particular a homogeneous
five-term equation alone is not the full-normal identity (13),
and a finite polynomial map is not a proof that its analytic
endpoint/ray chains may be discarded.

## Complete direct sources

- [C] [Exact nine-cell evaluation](research_nine_cell_canonical_crossing_evaluation.md),
  SHA256 332062e67d64ab4a0767637c0fdd96f186d62c430ad38042aef35ad857d8d7c9.
- [B] [Literal charged inverse and bubble](research_literal_charged_tetrahedron_bubble.md),
  SHA256 1dfe35f26137572235b1c3af66dcf410e0af758836baddaa8dd6d958c0f61d9b.
- [S] [Literal nine-cell source](research_nine_tetrahedron_boundary_source_reduction.md),
  SHA256 5aeecb0c174f33baa1264bc34c7419d4ccae007e84f4410b3dcb47c6c81c554c.

All three complete texts were freshly read and their used implications
checked. No mathematical program or numerical experiment was used.
