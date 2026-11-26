# Exact terminal recurrences and a bulk transfer upper bound

Private written proof, 16 November 2026.

For a fixed signed turn, the original terminal eigenvector and its
Jordan companion satisfy an exact finite physical-row system.
Their values and first normals propagate across any compact
interior interval with an upper bound given by the integrated
maximum characteristic growth, up to a polynomial factor and
\(\exp(O(\sqrt N))\). The double characteristic roots are retained.
No endpoint initialization, selected-branch lower coefficient,
or closed-source estimate is inferred.

## 1. Original source and the exact physical operator

Use the full original algebra and carriers
\[
 \mathcal A_N=\mathbb C[Z]/(P_N),\qquad
 P_N(Z)=2T_N(Z/2)+2,\qquad q=e^{\pi i/N},\qquad
 c_0=q+q^{-1},\qquad \kappa=q^{(N-1)^2/2}.
\]
Here \(T_N\) is Chebyshev's polynomial, whereas \(T,R\) are
the original physical turn and crossing. The notation \(K_N\)
means the original symmetric Newton kernel with the
normalization of the operator source. Every noninteger
power below uses \(q^z=\exp(\pi iz/N)\). Put
\[
 C f=Zf\pmod {P_N},\quad J=TCT,\quad
 V_n=\kappa^nTR^{-n}T,\quad D_n=V_nCV_{-n},
\]
\[
 G_n=T(R^{-n}),\qquad H_n=T(R^{-n}Q_N),\qquad
 Q_N(Z)=\left.\partial_w K_N(w,Z)\right|_{w=c_0}.
 \tag{1}
\]
All these are ordinary canonical polynomials when appropriate.
The exact source identities are
\[
 (D_n-c_0)G_n=0,\qquad (D_n-c_0)H_n=G_n.                 \tag{2}
\]
In particular \(H_n\) is not obtained by replacing \(Q_N\)
by \(TQ_N\), nor is its forcing suppressed.

Fix \(n=\sigma m\), with \(\sigma\in\{1,-1\}\), \(m\ge1\).
Write \(h=N^{-1}\), and use the scaled physical row coordinate
\[
 u_j=j/N,\qquad c_N(u)=2\cos(2\pi u+\pi/N).
 \tag{3}
\]
Choose a closed interval \(I=[a,b]\subset(0,1/2)\), and
reserve a larger closed interval strictly inside \((0,1/2)\).
Every statement below is uniform on \(I\), with this fixed
buffer. Only sufficiently large \(N\) is needed.

For a possibly noninteger index \(j\), let
\[
 s_j=2\sin(j\pi/N),\quad
 A_j=\frac{s_{j+1}^4}{s_{2j+1}s_{2j+2}},\quad
 C_j^{\rm row}=\frac{s_j^4}{s_{2j}s_{2j+1}}.
 \tag{4}
\]
The superscript distinguishes the scalar row coefficient
from spectral multiplication \(C\). The ordinary difference
operator representing \(J\) is
\[
 (\widetilde J f)(c_N(u))
  =(c_0+A_{Nu}+C_{Nu}^{\rm row})f(c_N(u))
    -A_{Nu}f(c_N(u+h))-C_{Nu}^{\rm row}f(c_N(u-h)).
 \tag{5}
\]
All coefficients in the buffered interval, with any fixed
number of derivatives in \(u\), are uniformly bounded.
Their apparent poles are outside a fixed complex neighborhood
of that interval, once \(N\) is large.

The physical formula for the first signed conjugation is
\[
 \begin{split}
 (\widetilde D_\sigma f)(c_N(u))
   ={}& A_{Nu}q^{-\sigma(2Nu+2)} f(c_N(u+h))\\
     &+\frac{8-c_N(u)(c_0+A_{Nu}+C_{Nu}^{\rm row})}{c_0}
                                                    f(c_N(u))\\
     &+C_{Nu}^{\rm row}q^{2\sigma Nu}f(c_N(u-h)).
 \end{split}                                             \tag{6}
\]
This is exact for \(N\ge3\). To check its phases, put
\(c_j=q^{2j+1}+q^{-2j-1}\), \(\Delta=q^2-q^{-2}\).
Then
\[
 q^{-1}c_{j+1}-qc_j=-q^{-2j-2}\Delta,\qquad
 q^{-1}c_{j-1}-qc_j=-q^{2j}\Delta.
 \tag{7}
\]
Insert these into
\(D_1=8I/c_0+(q^{-1}JC-qCJ)/\Delta\).
The diagonal uses
\((q^{-1}-q)/\Delta=-1/c_0\).
Coefficient conjugation gives \(\sigma=-1\).

Define ordinary operators for \(k\ge0\) by
\[
 \widetilde D_0=\widetilde C,\qquad
 \widetilde D_{\sigma(k+2)}
   =8q^{-\sigma}I-q^{-2\sigma}\widetilde D_{\sigma k}
            -q^{-\sigma}\widetilde D_{\sigma(k+1)}
                                      \widetilde J,        \tag{8}
\]
where \(\widetilde C\) means ordinary multiplication by \(Z\).
Their action has the finite form
\[
 (\widetilde D_n f)(c_N(u))
     =\sum_{k=-m}^{m} b_{n,k,N}(u)f(c_N(u+kh)).
 \tag{9}
\]
The coefficients are completely defined by (5)--(8), with
the indicated right ordering. In particular a coefficient
of \(\widetilde J\) in a product is evaluated at the shifted
row, not at the unshifted row.

**Lemma 1.** The two extreme coefficients in (9) are exactly
\[
 \begin{split}
 b_{n,m,N}(u)
    &=q^{-\sigma(2Nu+m+1)}
                       \prod_{\ell=0}^{m-1}A_{Nu+\ell},\\
 b_{n,-m,N}(u)
    &=q^{\sigma(2Nu-m+1)}
                       \prod_{\ell=0}^{m-1}C_{Nu-\ell}^{\rm row}.
 \end{split}                                             \tag{10}
\]
They are bounded away from zero on a common complex
neighborhood of \(I\), uniformly for all sufficiently large
\(N\). Every coefficient in (9) has a holomorphic expansion
there with an \(O(N^{-1})\) error from its leading symbol,
including any fixed number of \(u\) derivatives.

*Proof.* At \(m=1\), (10) is (6). In the next step of (8),
only the product with \(\widetilde J\) can reach the new
extreme shifts. Its forward coefficient multiplies the
previous extreme coefficient by \(q^{-\sigma}A_{Nu+m}\);
the backward one multiplies by
\(q^{-\sigma}C_{Nu-m}^{\rm row}\). This proves both phases
and products by induction.

Uniformly on a fixed complex neighborhood of the buffer,
\[
 A_{Nu+\ell}=\tan^2(\pi u)+O(N^{-1}),\qquad
 C_{Nu+\ell}^{\rm row}=\tan^2(\pi u)+O(N^{-1})             \tag{11}
\]
for every fixed \(\ell\). The limiting function is a unit
there after the neighborhood is decreased. All denominators
in (4) and \(c_0\) are likewise units. Equations (5)--(8)
give the remaining assertions by finitely many products,
shifts, and sums. Cauchy estimates on a slightly larger
neighborhood give the derivative assertions. \(\square\)

The ordinary operators in (8) descend to the original
canonical \(D_n\). Indeed the original difference operator
maps ordinary polynomials to polynomials, and
\[
 \widetilde J(P_N f)=P_N\widetilde J f.                    \tag{12}
\]
This follows from \(P_N(c_N(u\pm h))=P_N(c_N(u))\).
Ordinary multiplication also preserves that ideal.
Thus (8) descends to the exact all-integer recurrence for
\(D_n\).

Consequently (2) implies that the ordinary residuals
\[
 (\widetilde D_n-c_0)G_n,\qquad
 (\widetilde D_n-c_0)H_n-G_n                              \tag{13}
\]
are multiples of \(P_N\). They need not vanish off the
physical grid. The identity
\[
                    P_N(c_N(u))=4\sin^2(\pi Nu)           \tag{14}
\]
shows that their values and first \(u\) derivatives vanish
at every interior grid point \(u_j\). This is the precise
reason that both original physical normal equations below
are exact; no off-grid eigen-equation is assumed.

## 2. The exact value and normal companion system

Put \(d=2m\), and define
\[
 a_{k,N}(u)=b_{n,k,N}(u)-c_0\mathbf1_{k=0},\qquad
 r_{k,N}(u)=-a_{k,N}(u)/b_{n,m,N}(u)\quad(-m\le k<m).
 \tag{15}
\]
Let \(\mathsf A_N(u)\) be the \(d\)-dimensional companion
matrix with upper shift rows and last row
\((r_{-m,N},\ldots,r_{m-1,N})\).
Let \(\mathsf B_N(u)\) have only one nonzero entry:
its last row, in column \(m\) when columns start at zero,
is \(b_{n,m,N}(u)^{-1}\).
Both matrices and their fixed derivatives are uniformly
bounded on the same neighborhood. The first coefficient
in the companion row is nonzero by (10); hence
\(\mathsf A_N^{-1}\) is uniformly bounded there as well.

For \(F=G_n\) or \(H_n\), write
\[
 F_j=F(c_N(u_j)),\qquad
 \dot F_j=c_N'(u_j)F'(c_N(u_j)),
\]
\[
 X_j^F=(F_{j-m},\ldots,F_{j+m-1})^{\mathsf T},\qquad
 Y_j^F=(\dot F_{j-m},\ldots,\dot F_{j+m-1})^{\mathsf T}.
 \tag{16}
\]
The prime on \(F\) is its ordinary spectral derivative;
the dot is the derivative in the scaled coordinate \(u\).
On the compact interval \(c_N'\) is a unit, so this
normalization neither discards nor degenerates a normal.

At every indicated interior row the exact source system is
\[
 \begin{split}
 X_{j+1}^{G}&=\mathsf A_N X_j^G,\\
 Y_{j+1}^{G}&=\mathsf A_N Y_j^G+\mathsf A_N'X_j^G,\\
 X_{j+1}^{H}&=\mathsf A_N X_j^H+\mathsf B_NX_j^G,\\
 Y_{j+1}^{H}&=\mathsf A_N Y_j^H+\mathsf A_N'X_j^H
                     +\mathsf B_NY_j^G+\mathsf B_N'X_j^G .
 \end{split}                                             \tag{17}
\]
All matrices on the right are evaluated at \(u_j\); their
primes mean \(u\) derivatives. To prove (17), solve the value
equations from (13) for the forward value at \(j+m\).
Differentiate that ordinary row equation and then evaluate
on the grid. Equation (14) removes the residual derivative.
This gives exactly the differentiated companion coefficients
in (17), including the derivative of the forcing coefficient.

For
\[
 \mathbb X_j=(X_j^G,Y_j^G,X_j^H,Y_j^H)^{\mathsf T},
\]
equation (17) is the homogeneous enlarged system
\[
 \mathbb X_{j+1}=\mathbb A_N(u_j)\mathbb X_j,\qquad
 \mathbb A_N=
 \begin{pmatrix}
 \mathsf A_N&0&0&0\\
 \mathsf A_N'&\mathsf A_N&0&0\\
 \mathsf B_N&0&\mathsf A_N&0\\
 \mathsf B_N'&\mathsf B_N&\mathsf A_N'&\mathsf A_N
 \end{pmatrix}.
 \tag{18}
\]
This notation does not turn \(H_n\) into an unforced
eigenvector: its original forcing is exactly the lower
coupling in (18). The grades of the four blocks are
\[
                            (0,1,1,2).                   \tag{19}
\]
Every nonzero off-diagonal block strictly increases grade.

## 3. Separated double characteristic roots

Let \(\mathsf A_0(u)\) be the leading matrix of
\(\mathsf A_N(u)\). The convergence
\[
                 \mathsf A_N=\mathsf A_0+O(N^{-1})         \tag{20}
\]
is uniform and holomorphic on a fixed neighborhood of \(I\).
Set \(\nu=2\pi u\), \(x=2\cos\nu\), and
\(a=\tan^2(\nu/2)\). The physical symbols of \(J,D_1\) are
\[
 y=2+2a-a(\tau+\tau^{-1}),\qquad
 z=2+2a+a(e^{-i\nu}\tau+e^{i\nu}\tau^{-1}).                \tag{21}
\]
The symbol \(x_n\) is defined by
\[
 x_0=x,\quad x_1=z,\quad
 x_{k+2}=8-yx_{k+1}-x_k
\]
for every integer \(k\).
The characteristic polynomial of \(\mathsf A_0(u)\) is the
monic polynomial obtained from
\(\tau^m(x_n-2)\) by dividing by its leading coefficient.
That coefficient is the nonzero limit of (10).

The adopted characteristic classification proves that this
polynomial has precisely \(m\) distinct nonzero roots
\(\tau_1(u),\ldots,\tau_m(u)\), each of multiplicity two.
They have holomorphic labels on a sufficiently small complex
neighborhood of \(I\); all are uniformly separated and
bounded away from zero and infinity there. This follows
also from its explicit simple reduced roots and the
nonsingular physical parametrization, so it does not apply
an implicit function theorem to an unreduced double root.

Define the continuous, locally Lipschitz real functions
\[
 L_+(u)=\max_{1\le \ell\le m}\log|\tau_\ell(u)|,\qquad
 L_-(u)=\max_{1\le \ell\le m}\log|\tau_\ell(u)^{-1}|.
 \tag{22}
\]
No choice of a single maximizing branch is made.
Crossings of moduli do not affect these definitions or
their Lipschitz property.

## 4. Quantitative Jordan scaling

Here is a direct matrix estimate for (18). It retains the
double roots instead of perturbatively diagonalizing them.
Put
\[
 v(t)=(1,t,\ldots,t^{d-1})^{\mathsf T},\qquad
 S(u)=\big(v(\tau_1),v'(\tau_1),\ldots,
                         v(\tau_m),v'(\tau_m)\big).
 \tag{23}
\]
The companion identity and the double-root condition give
\[
 \mathsf A_0v(\tau_\ell)=\tau_\ell v(\tau_\ell),\qquad
 \mathsf A_0v'(\tau_\ell)
             =v(\tau_\ell)+\tau_\ell v'(\tau_\ell).
 \tag{24}
\]
The confluent Vandermonde determinant is nonzero because
the roots are separated. Thus \(S,S^{-1}\), and their fixed
derivatives are uniformly bounded on a smaller neighborhood.
In this frame \(\mathsf A_0\) is the direct sum of
\(\left(\begin{smallmatrix}\tau_\ell&1\\0&\tau_\ell\end{smallmatrix}\right)\).

Write \(\epsilon=N^{-1/2}\), and set
\[
 E_\epsilon=\operatorname{diag}(1,\epsilon,\ldots,1,\epsilon),
 \qquad S_\epsilon=S E_\epsilon .
 \tag{25}
\]
Within each two-dimensional block the superdiagonal becomes
\(\epsilon\). The finite-\(N\) perturbation in (20) becomes
\(O(N^{-1}/\epsilon)=O(\epsilon)\).
The change of frame over one row also satisfies
\[
 S_\epsilon(u+h)^{-1}S_\epsilon(u)
                          =I+O(h/\epsilon)=I+O(\epsilon).
 \tag{26}
\]
Therefore the diagonal block of the transformed one-step
system is a diagonal matrix with entries \(\tau_\ell(u)\),
each twice, plus \(O(\epsilon)\).

To include all the source and normal couplings, use
\[
 \mathbb S_N(u)
  =\operatorname{diag}
      \big(S_\epsilon(u),\,N S_\epsilon(u),\,
                N S_\epsilon(u),\,N^2 S_\epsilon(u)\big).
 \tag{27}
\]
This is exactly the grade choice (19).
A bounded block from grade \(g\) to grade \(g'>g\)
is multiplied under this similarity by
\(N^{g-g'}\). Its remaining \(S_\epsilon\) conditioning
cost is at most \(O(\epsilon^{-1})\). It is consequently
\(O(N^{-1}\epsilon^{-1})=O(\epsilon)\), or smaller.
This applies to every entry
\(\mathsf A_N',\mathsf B_N,\mathsf B_N'\) in (18);
none had to be small before the similarity.
In particular
\[
 \left\|\mathbb S_N(u+h)^{-1}\mathbb A_N(u)
                            \mathbb S_N(u)\right\|
                  \le e^{L_+(u)}+C N^{-1/2}.              \tag{28}
\]
Use the Euclidean operator norm, for example. The diagonal
part has norm \(e^{L_+}\), and the fixed number of error
blocks changes that by at most \(CN^{-1/2}\).
The endpoint frame costs satisfy
\[
 \|\mathbb S_N(u)\|\le CN^2,\qquad
 \|\mathbb S_N(u)^{-1}\|\le CN^{1/2}.                     \tag{29}
\]
All constants depend on \(n,I\) and its buffer, not on \(N\).

The inverse matrix has the same graded triangular structure,
with uniformly bounded off-diagonal blocks and diagonal
\(\mathsf A_N^{-1}\). In the frame (25) its leading diagonal
is \(\tau_\ell^{-1}\), with \(O(\epsilon)\) error.
The same reasoning with the backwards frame change gives
\[
 \left\|\mathbb S_N(u)^{-1}\mathbb A_N(u)^{-1}
                            \mathbb S_N(u+h)\right\|
                  \le e^{L_-(u)}+C N^{-1/2}.              \tag{30}
\]
The nonzero extreme coefficient in (10) is essential here.

## 5. The integrated upper bound and its limits

**Theorem 2.** Fix \(n\ne0\) and \(I\Subset(0,1/2)\).
There are constants \(C,N_0\), depending only on this
choice and a fixed interior buffer, such that the exact
system (18) has the following propagator bounds for all
\(N\ge N_0\) and all \(j\le k\) with \(u_j,u_k\in I\):
\[
 \boxed{\begin{split}
 \|\Phi_N(k,j)\|
   &\le C N^{5/2}
       \exp\left\{
          N\int_{u_j}^{u_k}L_+(u)\,du
                       +C\frac{k-j}{\sqrt N}+C\right\},\\
 \|\Phi_N(j,k)\|
   &\le C N^{5/2}
       \exp\left\{
          N\int_{u_j}^{u_k}L_-(u)\,du
                       +C\frac{k-j}{\sqrt N}+C\right\}.
 \end{split}}                                             \tag{31}
\]
Here \(\Phi_N\) is the product of the literal finite-\(N\)
matrices (18), not the limiting matrix product. In particular
the actual original vector \(\mathbb X_j\) obeys these
inequalities with its actual initial data.

*Proof.* Multiply (28) over the indicated rows and use (29).
The positive function \(e^{L_+}\) is uniformly bounded away
from zero, so
\[
 \log(e^{L_+(u)}+CN^{-1/2})
                   \le L_+(u)+C'N^{-1/2}.
 \tag{32}
\]
Since \(L_+\) is Lipschitz on the compact interval,
the difference between its row sum and
\(N\int_{u_j}^{u_k}L_+\) is bounded uniformly.
This proves the first inequality. Use (30) in the reverse
order for the second. No estimate of an individual
connection coefficient enters the proof. \(\square\)

Thus the transfer upper rate over a fixed interior interval is
the integral of the maximum logarithmic modulus, with an
explicit \(O(\sqrt N+\log N)=o(N)\) loss.
The coupling from \(G_n\) into \(H_n\), and both original
first-normal channels, are all inside this same bound.
The double characteristic roots have not been replaced by
simple branches or omitted as negligible.

For \(n=0\), the separate equation \(D_0=C\) gives
\((C-c_0)G_0=0\), \((C-c_0)H_0=G_0\).
At every double physical node other than \(c_0\), their
values and first normals vanish. Hence their compact
interior data are zero, and no companion recurrence is
required for that case.

The constants and analytic neighborhoods here need not
remain uniform as \(u\) tends to \(0\) or \(1/2\).
The first physical coefficient \(C_j^{\rm row}\) vanishes
at \(j=0\), and other endpoint charts have their own
degeneracies. Formula (10) proves the required interior
unit property; it does not bypass those endpoint issues.
The theorem therefore neither initializes the source from
its endpoint data nor determines which reduced branch
actually appears. It gives no lower bound, noncancellation
statement, relative-cycle coefficient, or whole graph rate.

## 6. Direct sources

The two complete direct sources were read at their frozen
versions, with the used identities and hashes checked:

* [Exact original operator and branching identities](research_unit_turn_finite_band_branching_operator.md),
  SHA256 31d9f574c7dc3aaac07e4eb50c131b3328be46b3c2a2ef46f9dae7f0c4ddb9cb:
  full algebra, ordinary ideal preservation, signed conjugation,
  all-integer recurrence, and original Jordan source (34)--(36).
* [All-power terminal characteristic geometry](research_terminal_twist_characteristic_geometry.md),
  SHA256 3606f43995336bc0481acf9e04a96da5efd65f67706bef42cc9b1b1011694d1b:
  physical symbols, analytic reduced branches, exact doubled
  characteristic multiplicity, and compact separation.

The finite extreme coefficients, full nodal-normal system,
and quantitative matrix scaling are proved above.
Only written mathematics, source text and hashes were used.
No mathematical program, numerical experiment, test, or build
was run. Frozen notes and public manuscripts are unchanged.
