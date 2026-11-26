# Quantitative control of the protected row and the remaining excursion bound

The finite excursion reduction preserves the original full-minus-CROSS
source, but nilpotence alone does not bound an excursion's size. This
note supplies a whole-real-spectral-interval bound for the complete
non-CROSS part of the protected marked row, with all boundary loads
retained. It also gives a single-low-Newton-profile bound for every
one-sided north coefficient and an exact polynomial bound for one
fully coupled two-step return block.

The natural local weighting by the complete circle parameters does
not turn every bad step into a contraction. We give its explicit
failure at the actual marked quartet and distinguish that failure
from the still-open estimate on a complete excursion.

## 1. Original source conventions

Use the same opposite-offset bipyramid as in the frozen excursion
note. The equator size \(m\ge6\) is even,
\[
 N\ge2,\qquad d=N-1,\qquad
 h=\lfloor d/2\rfloor,\qquad
 M=\lfloor N/2\rfloor-1,\qquad q=e^{\pi i/N},
 \tag{1}
\]
and
\[
 s_r=2\sin(r\pi/N),\quad S_r=\prod_{k=1}^r s_k,\quad
 c_r=q^{2r+1}+q^{-2r-1},\quad
 \chi_N(z)=2T_N(z/2)+2.
 \tag{2}
\]
Here \(M\) is an integer cutoff, not a meridian variable.
The original face operator and its full numerator are
\[
 C(x,y)z^r=c_rz^r-s_r^2(x+y)z^{r-1}
                         -s_rs_{r-1}xy z^{r-2},\qquad
 V_N(\sigma;C)=\frac{\chi_N(\sigma)-\chi_N(C)}{\sigma-C}.
 \tag{3}
\]
The second expression is polynomial functional calculus, with all
double-root normals retained. No inverse at a spectral node is
introduced.

The north coupons have outer variables \(0,z_j\). The protected
marked one, at row \(1\), is
\(H_{V_N}(0,0,z_2,z_1;\sigma)\). Its coefficient of
\(z_1^\ell z_2^{d-\ell}\) is
\[
 v_\ell(\sigma)
 :=V_N(\sigma;C(0,1))_{0,\ell}
 =(-1)^\ell S_\ell^2
                   \prod_{r=\ell+1}^{d}(\sigma-c_r).
 \tag{4}
\]
The formula follows from the unique one-step path of the bidiagonal
matrix \(C(0,1)\), including all unused diagonal factors.
The marked coupon is non-CROSS precisely for
\(0\le\ell\le M\). At odd level the central row is CROSS
and is not included in this range.

The polynomial statements below hold at \(N=2\) as well. Their
physical general-Morse source application uses the existing exact
source identity in its stated range \(N\ge3\), with the original
protected faces and component, cup, cap, and mark normalization.

## 2. An exact positive Laurent factorization of the marked bad row

For \(0\le\ell\le M\), put \(n=N-2\ell-2\ge0\), and define
\[
 B_n(u)=\prod_{r=0}^{n-1}(u+q^{2r-n+1})
       =\sum_{k=0}^n\frac{S_n}{S_kS_{n-k}}u^k.
 \tag{5}
\]
Every coefficient on the right is positive because \(n<N\).
The coefficient identity can be proved by induction from
\[
 B_{n+1}(u)=(q^n u+1)B_n(q^{-1}u),\qquad
 s_{n+1}=q^{n+1-k}s_k+q^{-k}s_{n+1-k}.
 \tag{6}
\]
Thus no positivity of an uncombined resolvent path expansion is
being assumed.

The exact factorization is
\[
 \boxed{\displaystyle
 v_\ell(u+u^{-1})
 =(-1)^\ell S_\ell^2 u^{\ell+1-N}(u^N+1)B_n(u).}
 \tag{7}
\]
Indeed
\(\chi_N(u+u^{-1})=u^{-N}(u^N+1)^2\), while
\[
 \prod_{r=0}^{\ell}(\sigma-c_r)
 =u^{-\ell-1}
   \prod_{r=0}^{\ell}(u-q^{2r+1})(u-q^{-2r-1}).
 \tag{8}
\]
The \(2\ell+2\) factors in (8) are distinct factors of \(u^N+1\).
The remaining roots form the consecutive arc centered at \(-1\),
and their monic product is exactly \(B_n(u)\). Substitution in
(4) proves (7) as a polynomial/Laurent identity, including all
spectral collisions.

After its common sign \((-1)^\ell\), the Laurent polynomial in
(7) has positive coefficients. Therefore
\[
 \sup_{-2\le\sigma\le2}|v_\ell(\sigma)|
                \le |v_\ell(2)|\le N^2.
 \tag{9}
\]
For the last inequality set
\[
 U_\ell=|v_\ell(2)|
 =\frac{4S_\ell^2}
           {\prod_{r=0}^{\ell}(2-c_r)},\qquad
 \frac{U_\ell}{U_{\ell-1}}
     =\frac{\sin^2(\ell\pi/N)}
                  {\sin^2((\ell+1/2)\pi/N)}.
 \tag{10}
\]
The latter ratio is at most one and then at least one, with
only one change. The endpoints are
\(U_0=\csc^2(\pi/(2N))\le N^2\) and \(U_d=N^2\).
The first bound uses
\(\sin(\pi/(2N))\ge1/N\), the elementary chord bound.
This proves (9), and in fact proves the endpoint bound in
(10) for every \(0\le\ell\le d\).

The Laurent degree of (7) is \(d-\ell\). Its positive coefficients
also give the fixed complex-strip estimate
\[
 |v_\ell(2\cos(\phi+iy))|
                  \le N^2e^{(d-\ell)|y|}
                  \qquad(\phi,y\in\mathbb R).
 \tag{11}
\]
This estimate preserves the original polynomial, not merely its
values at the root nodes.

## 3. A whole marked-row operator bound with all boundary loads

The incoming transfer state at row \(1\) is \((0,v)\),
\(0\le v\le d\). The complete non-CROSS part of that row,
denoted \(R_N(\sigma)\), has exactly the entries
\[
 (R_N(\sigma))_{(0,v),(v+\ell,d-\ell)}
       =v_\ell(\sigma),\qquad
 0\le\ell\le\min(M,d-v).
 \tag{12}
\]
Every other entry is zero. This is the literal marked transfer,
not a reset of the incoming grade. Its grade increases by \(d\),
as required by the protected target.

Each row of (12) has at most \(M+1\) entries. Each column has at
most one: it determines \(\ell=d-v'\) and then
\(v=u'-\ell\). Consequently, uniformly on the full real
spectral interval,
\[
 \boxed{\displaystyle
 \|R_N(\sigma)\|_1\le N^2,\qquad
 \|R_N(\sigma)\|_\infty\le(M+1)N^2,\qquad
 \|R_N(\sigma)\|_2\le N^2\sqrt{M+1}.}
 \tag{13}
\]
Here the first two are the induced column- and row-sum norms;
the third is the Euclidean operator norm. The latter follows
directly from
\(\|A\|_2^2\le\|A\|_1\|A\|_\infty\), or from weighted
Cauchy applied to each row and then summed over columns.

The outgoing state is always bad. Conversely, a valid marked
transition with bad incoming state cannot end in a good state:
if \(v>h\), then \(\ell\le d-v\le M\), so the outgoing
middle exponent \(d-\ell\) is high. Hence (13) bounds both
the good-to-bad marked block and the bad-to-bad marked block.
It retains every incoming load, including those above \(h\).

There is no analogous conclusion here for an arbitrary
unprotected one-sided coupon. Its incoming middle exponent
need not be zero.

## 4. The exact remaining north profile

Let
\[
 e_i(\sigma)=S_i^{-2}\prod_{r=0}^{i-1}(c_r-\sigma).
 \tag{14}
\]
The bidiagonal resolvent has the exact semiseparable formula
\[
                   V_N(\sigma;C(0,1))_{i,j}
                          =e_i(\sigma)v_j(\sigma)
                          \qquad(0\le i\le j\le d).
 \tag{15}
\]
One proves it directly from the unique interval path:
the prefactor is
\((-1)^{j-i}(S_j/S_i)^2\), with the unused prefix and suffix
left intact. The reflected identity
\[
                V_{i,j}=V_{d-j,d-i}
 \tag{16}
\]
follows from \(c_{d-r}=c_r\) and the reflected sine coefficients,
or from the original anti-diagonal adjoint relation.

Suppose a north monomial has middle powers \(a,c\), with one
of them high. Put \(i=\min(a,c)\), \(j=d-\max(a,c)\).
Then \(0\le i\le j\le M\), and its exact scalar coefficient is
\(e_i(\sigma)v_j(\sigma)\). Low Newton positivity gives
\[
 \sup_{[-2,2]}|e_i(\sigma)|=e_i(-2),\qquad
 |H^{\mathrm{NC}}_{\mathrm{north}}[a,c](\sigma)|
                            \le N^2 e_i(-2).
 \tag{17}
\]
For completeness, the first assertion follows by the same
finite product as (5):
\[
 e_i(-u-u^{-1})=S_i^{-2}u^{-i}B_{2i}(u).
 \tag{18}
\]
All its Laurent coefficients are positive because \(2i<N\).

Thus one low Newton profile, rather than an uncontrolled whole
one-sided interval, contains all possible exponential size of a
north non-CROSS coefficient. This is not a polynomial bound on
that coefficient: for bulk \(i\), the factor \(e_i(-2)\) is
exponentially large. With the original sine-product normalization,
its closed rate is
\[
 \frac1N\log e_i(-2)
    =g(i/N)+O(\log N/N),\qquad
 g(x)=J(2x)-4J(x),\quad
 J(x)=\int_0^x\log(2\sin\pi t)\,dt .
 \tag{19}
\]
The estimate is uniform for the displayed low range, by
truncated logarithmic Riemann sums. Formula (17) keeps this
profile explicitly; it is not discarded as a polynomial factor.

## 5. The actual two-step return and one fully bounded boundary sector

Consider a return in two steps, through the marked north row \(1\)
and the adjacent south row \(2\). Keep its incoming good state
\((0,\alpha)\), and its outgoing good state
\((d-\beta,i)\), where \(0\le\alpha,\beta,i\le h\).
The south power is forced, not freely assigned:
\[
                         p=\alpha+\beta-i.
 \tag{20}
\]
If \(p<0\), the entry is zero. Otherwise the exact two-step
bad-excursion entry is
\[
 \boxed{\displaystyle
 E_{\alpha;\beta,i}(\sigma,\tau)
 =[S^p]\sum_{\ell=\beta}^{M}
       v_\ell(\sigma)
       V_N(\tau;C(S,1))_{i,\ell+\alpha}.}
 \tag{21}
\]
An empty interval gives zero. To verify every index, the
intermediate state is
\((\alpha+\ell,d-\ell)\). The second coupon consequently has
middle powers \(d-\alpha-\ell,i\), central outer power
\(\ell-\beta\), and south power \(p\). All are original
nonnegative powers. Its reversed physical middle order gives
exactly the matrix entry in (21).

In the boundary sector \(\alpha=\beta=i=0\), the common
south power is zero and \(C(0,1)\) is bidiagonal. Hence
\[
 E_{0;0,0}(\sigma,\tau)
      =\sum_{\ell=0}^{M}v_\ell(\sigma)v_\ell(\tau),\qquad
 \boxed{\displaystyle
 \sup_{\sigma,\tau\in[-2,2]}|E_{0;0,0}(\sigma,\tau)|
                         \le(M+1)N^4.}
 \tag{22}
\]
This holds for both parities and for both spectral variables
throughout the interval. It combines the entire actual
two-step boundary sum before estimating it. No neighbor is
fixed to \(-2\), and no aligned two-row source is substituted
for the opposite-offset source.

The remaining south target \(S^d\) must still be supplied
by the other original rows. Formula (22) does not replace
that target or bound all boundary sectors of (21). In
particular, when \((\alpha,\beta,i)\ne(0,0,0)\), the
remaining coefficient in (21) can contain a long
two-outer-face interval. The uniform estimate currently
available from (9) is only
\[
 |E_{\alpha;\beta,i}|
 \le N^2\sum_{\ell=\beta}^{M}
       \left|[S^p]V_N(\tau;C(S,1))_{i,\ell+\alpha}\right|.
 \tag{23}
\]
The exact signed sum (21), not an assumed Gram pairing of
arbitrary neighboring coupons, is the object that would
need a stronger correlated bound.

## 6. Why the direct geometric one-step norm is not a contraction

For the original north-spoke mark, normalize its neighboring rim
circle parameter to one. The actual protected quartet is
\[
                       (x,b,c,y)=(0,0,r,1),
 \qquad r=4\cos^2(\pi/m)\ge3.
 \tag{24}
\]
The complete CROSS local potential in the original source
normalization is
\[
 X_{\mathrm{mark}}=F(r),\qquad
 F(r)=\frac2\pi\operatorname{Ti}_2(\sqrt r),\qquad
 \operatorname{Ti}_2(t)=\int_0^t\frac{\arctan u}{u}\,du.
 \tag{25}
\]
The geometric face-weighted marked transfer contains the
bad entry from \((0,0)\) to \((0,d)\). At even level and
\(\sigma=-2\), its absolute value is exactly
\[
                  r^d\sec^2(\pi/(2N)).
 \tag{26}
\]
Indeed this is the pure-middle term \(c^d v_0(-2)\), with
the original unused factors retained.

Normalize this local matrix by its proposed complete
budget \(e^{NX_{\mathrm{mark}}}\). Any induced coordinate
\(\ell^p\) norm is at least the magnitude of one matrix
entry. Equations (25),(26) imply
\[
 \liminf_{\substack{N\to\infty\\N\ \mathrm{even}}}
   \frac1N\log
   \left\|e^{-NF(r)}R_N^{\mathrm{geometric}}(-2)\right\|
                    \ge\log r-F(r)>\frac1{10}.
 \tag{27}
\]
For the last strict bound, the elementary reciprocal identity
for the inverse-tangent integral gives
\[
 F(r)-\log r
   =\frac2\pi\operatorname{Ti}_2(r^{-1/2})
          -\frac12\log r
   <\frac2{\pi\sqrt3}-\frac12\log3<-\frac1{10}.
 \tag{28}
\]
Here \(\operatorname{Ti}_2(t)<t\), \(\pi>3\),
\(\sqrt3>5/3\), and \(\log3>1\) suffice.

This refutes the specified *one-step* contraction in the
geometric incidence weights. It does not refute an
additional state-dependent boundary norm obtained after
contracting neighboring rows, or a bound for a whole
excursion. In fact, (13) shows that the unweighted marked
bad row itself is only polynomially large. The exponential
cost in (27) is the imposed face weight for the high
middle load. Its compensation must occur in the
remaining, correlated source.

The previously proved positive Cauchy capacity obstruction
already excludes a different, coarser remedy: replacing
every full local polynomial by its unconditioned positive
value at one shared set of radii cannot give the sharp
complete rate at an unbalanced packing. It does not
exclude the conditional matrix estimate sought here.

## 7. An internal bad-state similarity cannot remove the excursion cost

Write the original position-clock transfer in good/bad blocks
\[
 L=\begin{pmatrix}A&B\\C&D\end{pmatrix},
 \qquad D^{3m}=0,\qquad
 K(z)=z^2B(I-zD)^{-1}C.
 \tag{29}
\]
For arbitrary invertible diagonal state weights \(S_P,S_Q\),
the block similarity is
\[
 A'=S_P^{-1}AS_P,\quad B'=S_P^{-1}BS_Q,\quad
 C'=S_Q^{-1}CS_P,\quad D'=S_Q^{-1}DS_Q.
 \tag{30}
\]
Consequently
\[
                    K'(z)=S_P^{-1}K(z)S_P.
 \tag{31}
\]
The bad-state weight \(S_Q\) cancels completely from the
coupled excursion. Since the bad directed graph is
acyclic, one can make the entries of \(D'\) arbitrarily
small by assigning rapidly varying weights along a
topological ordering. Equation (31) proves why that
operation alone cannot yield a bound on the actual
source: the incoming and outgoing factors pay the
compensating costs.

Thus the next useful estimate must concern the signed
matrix \(K(z)\) in a controlled good-state boundary norm,
or its actual contractions with the good-state transfer.
A small norm for the nilpotent bad block by itself is
not such an estimate.

## 8. Relation to the existing source estimates and remaining scope

The complete positive endpoint and its small complex
polydisk complement have already been proved under
their stated original-source hypotheses. They are not
reproved here. In particular the existing flat-plat
theorems cannot be silently applied to an arbitrary
matched-sphere Morse presentation without the additional
source and geometry adapter.

The all-CROSS cofactor bounds already control their
original spectral strip and angular torus, retaining
the protected cofactor cases. Those results cannot
be substituted for the unused prefix and suffix
factors of a general one-sided interval. Formula (7)
is a special exact cancellation of those factors
at the protected first row; (17) states precisely
what remains for the other north rows.

Absolute estimates of individual complementary-source
tree channels can exceed the geometric rate, even
after their forced full contractions. Therefore no
termwise tree-channel estimate is used in deriving
(13) or (22).

All displayed bounds preserve the original root
polynomials and their spectral normals. They may be
differentiated in the spectral variables with the
usual fixed-degree polynomial costs. They cannot
be differentiated in \(q\) while retaining the
same root cutoff and omitted endpoint arrows.
No whole-cube bound for the full sewn difference,
and no new filled-knot volume theorem, follows
from the present local and boundary estimates.
