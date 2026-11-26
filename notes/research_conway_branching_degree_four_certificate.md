# A degree-four certificate on the branching packets

21 November 2026. Research note. Earlier finals and public manuscripts
remain unchanged.

Exact removal of the linear branches preserves more than the quartic
objective. Its minimum still has a degree-four sum-of-squares certificate
on the original \(2q\) packet balls. No redundant quartic constraints or
higher-order moment hierarchy are needed.

The reason is specific to the normalized source: after the prescribed
leaf packets are inserted, every intervening linear map is small. Its
exact covariance stays close to the identity. Whitening these known
covariances gives another small-tensor tree, to which the original
Hessian certificate applies. A linear pullback returns the certificate
to the original retained variables and normalization.

## 1. The exact branching problem

Fix \(N\ge2\), and put \(\sigma=1/16\). Every packet is the full
complex \(N\)-dimensional Newton space, with its positive coefficient
norm and all Casimir first normals. The original local tensors have
Hilbert--Schmidt norm at most \(\sigma\).

Start from the already clamped internal-edge quartic. Its prescribed
leaf-to-product transports have norm at most \(\sigma\); no unknown
binary-subtree output is clamped. Retain the two inputs of each product
with two internal inputs. If there are \(q\) such products, these are
\(2q\) distinct packets \(w\), or \(n=4Nq\) real coordinates.
The branching theorem gives a known real quartic \(F(w)\), with
\[
 m=\min_{\|w_i\|\le1}F(w),\qquad
 B_{\rm tot}^2m\le |K_N|^2
              \le\frac{197}{196}B_{\rm tot}^2m.
 \tag{1}
\]
Its minimum is unique and interior. All original phases, closing
data and the same budget \(B_{\rm tot}\) remain.

We first describe the exact coefficients of this smaller tree.
Before its final linear elimination the clamped objective is a sum of
nonroot costs
\[
 \|y_{\rm out}-P_v\Phi_v(y_L,y_R)\|_{W_v^{-1}}^2,
       \qquad I\le W_v\le C_1I,\quad C_1=\frac{256}{255},
 \tag{2}
\]
and one scalar root square with its recorded positive denominator
\(D_*\ge1\). Here \(\|P_v\|\le1\), and either input may be a
prescribed leaf transport. The weighted norm is \(u^*W_v^{-1}u\).

If a product has only one internal input, its known linear map has
Hilbert--Schmidt norm at most
\[
        \|P_v\Phi_v(f_v,\cdot)\|_{\rm HS}
                \le\|\Phi_v\|_{\rm HS}\|f_v\|\le\sigma^2.
 \tag{3}
\]
A product with no internal inputs is a known constant of norm at
most \(\sigma^3\). The products with two internal inputs retain their
bilinear coefficient norm at most \(\sigma\).

## 2. Exact chain covariances and the original root denominator

The omitted components really are chains. Every product with two
unfixed inputs has both inputs retained. Every other product has at
most one unfixed input, and every output has only one parent.
Starting at a constant forcing or a retained-input bilinear forcing,
follow these one-input products upward until a retained output or
the scalar root is reached. These chains contain every residual
exactly once; adjacent branching products give a chain of length zero.

Consider one chain ending at a retained packet \(y_m=w_i\). Its cost is
\[
 \|y_0-f(w)\|_{W_0^{-1}}^2+
              \sum_{j=1}^m\|y_j-A_jy_{j-1}\|_{W_j^{-1}}^2,
             \qquad \|A_j\|\le\sigma^2 .
 \tag{4}
\]
Its initial forcing is a known constant or one genuine bilinear
product of retained inputs. Define
\[
 \Pi_j=A_m\cdots A_{j+1},\quad\Pi_m=I,\quad\Pi=\Pi_0,\qquad
                    \mathcal W_i=\sum_{j=0}^m\Pi_jW_j\Pi_j^* .
 \tag{5}
\]
Writing the errors in (4) as \(r_j\) gives
\(w_i-\Pi f=\sum_j\Pi_jr_j\). Their exact least weighted-square
cost is therefore
\[
                 \|w_i-\Pi f(w)\|_{\mathcal W_i^{-1}}^2 .
 \tag{6}
\]
Indeed the minimizing errors are
\(r_j=W_j\Pi_j^*\mathcal W_i^{-1}(w_i-\Pi f)\).
They satisfy the endpoint equation and minimize by completing the
square. The original omitted balls are inactive by the branching
theorem, so this is the original constrained partial minimum.

The last summand in (5) is \(W_m\ge I\), and (3) gives
\[
 I\le\mathcal W_i\le C_0I,\qquad
 C_0=\frac{C_1}{1-\sigma^4}
            =\frac1{(1-\sigma^2)(1-\sigma^4)}<\frac{16}{15}.
 \tag{7}
\]
The effective forcing \(\Pi f\) keeps coefficient norm at most
\(\sigma\); a constant forcing has norm at most \(\sigma^3\).
No budget is reassigned to this composed map.

The final chain is terminated by the original scalar cost
\(|\ell y_m|^2/D_*\), with its full known row and denominator.
The same error calculation gives
\[
 \frac{|\ell\Pi f(w)|^2}{\mathcal D},\qquad
 \mathcal D=D_*+\sum_j\ell\Pi_jW_j\Pi_j^*\ell^*\ge1.
 \tag{8}
\]
This formula also follows by minimizing
\(\sum_j\|r_j\|_{W_j^{-1}}^2+
 |\ell\Pi f+\sum_j\ell\Pi_jr_j|^2/D_*\).
If the highest genuine branching product is itself the original
top product, its original bilinear scalar root square is used
directly, without adding an artificial output residual.

In either case the root term is \(|g(w_L,w_R)|^2\) with bilinear
coefficient norm at most \(\sigma^2\): its closing row has norm at
most \(\sigma\), its initial product at most \(\sigma\), subsequent
linear maps have norm at most one, and its denominator is at least
one. Every known phase and the original \(D_*\) are retained.

For \(q\ge1\), the resulting tree has \(q-1\) nonroot bilinear
gates, \(q+1\) constant gates, and the one scalar bilinear root.
Its \(2q\) proper output packets are exactly \(w\).

## 3. Whitening gives a small-tensor Hessian certificate

For each retained packet make the known linear change
\[
                    w_i=\mathcal W_i^{1/2}x_i .
 \tag{9}
\]
The original unit ball becomes the ellipsoid
\[
              e_i(x)=1-x_i^*\mathcal W_i x_i\ge0,
 \tag{10}
\]
which is contained in the unit ball of \(x_i\). Equations (6) and
(8) turn the objective into
\[
 \widetilde F(x)=
       \sum_{i\ {\rm proper}}\|\widetilde\Phi_i(x_{\rm children})-x_i\|^2
                           +|\widetilde g(x_L,x_R)|^2 .
 \tag{11}
\]
Every bilinear coefficient array in a proper gate has norm at most
\(C_0\sigma\), since the two input square roots each cost at most
\(\sqrt{C_0}\) and the output inverse square root costs at most one.
The root coefficient norm is at most \(C_0\sigma^2\); the constant
gates stay smaller. Consequently every such coefficient norm is
less than
\[
                            \rho=\frac1{12}.
 \tag{12}
\]

The algebraic Hessian proof for the original degree-four certificate
now applies to (11), with one minor root change. At the scalar
bilinear root its half-Hessian is
\[
 |D\widetilde g(x)h|^2+
       2\operatorname{Re}\bigl(\overline{\widetilde g(x)}
                                      \,\widetilde g(h_L,h_R)\bigr).
 \tag{13}
\]
The first term is a square. Identity (7) of the direct Hessian proof
controls the second with allowance
\(\rho^2(\|h_L\|^2+\|h_R\|^2)\), plus its unit-ball multipliers.
There is no negative output-curvature term at this root.

The same allowances for the proper gates are at most
\(3\rho+\rho+\rho^2\) per squared variation norm. Each child has
one parent, including the root, so the sibling-pair count is unchanged.
The result is the polynomial identity
\[
 h^{\mathsf T}(D^2\widetilde F-\alpha I)h
   =\sum_\nu|A_\nu(x)h|^2+
                \sum_i(1-\|x_i\|^2)h^{\mathsf T}C_i h,
       \qquad \alpha=2(1-4\rho-\rho^2)=\frac{95}{72},
 \tag{14}
\]
where the \(A_\nu\) are affine and \(C_i\) constant positive
semidefinite real matrices. All coordinates and variations here
are real and imaginary parts of the original complex packets.

Replace each unit-ball factor by
\[
             1-\|x_i\|^2=e_i(x)+x_i^*(\mathcal W_i-I)x_i .
 \tag{15}
\]
The added term times \(h^{\mathsf T}C_i h\) is a sum of squares
of bilinear forms in \(x,h\). Pull (14) back through (9).
Then \(e_i\) is the original ball
\(g_i(w)=1-\|w_i\|^2\), and
\(\alpha\mathcal W_i^{-1}-I\succeq0\), since
\(\alpha>16/15>C_0\). Adding this constant squared variation
form proves the original-variable identity
\[
 h^{\mathsf T}(D^2F-I)h
   =\sum_\nu|B_\nu(w)h|^2+
                        \sum_i g_i(w)h^{\mathsf T}D_i h ,
 \tag{16}
\]
with affine \(B_\nu\) and constant \(D_i\succeq0\).
This is the required degree-two Hessian module certificate on
the original retained balls.

## 4. Exact degree-four optimization and trial certificates

Let \(Q_2(g)\) be sums of squares of polynomials of degree at most
two, plus \(\sum_i g_i\) times sums of squares of linear polynomials.
Integrating (16) along the line from a feasible retained trial \(u\)
to \(w\) proves
\[
 F(w)-F(u)-\nabla F(u)\cdot(w-u)-\tfrac12\|w-u\|^2
                                                      \in Q_2(g).
 \tag{17}
\]
Indeed the ball identity along that line is
\[
 g_i((1-t)u+tw)=(1-t)g_i(u)+t g_i(w)+t(1-t)\|w_i-u_i\|^2.
 \tag{18}
\]
Its first and last terms contribute sums of squares; the middle
term is the original ball times a sum of squares of linear polynomials. Integrals of
squared affine-matrix forms have positive semidefinite finite Gram
matrices and preserve degree four.

At the unique interior minimizer \(w_*\), (17) gives
\[
 F-m-\tfrac12\|w-w_*\|^2\in Q_2(g),\qquad
                  m=\max\{\lambda:F-\lambda\in Q_2(g)\}.
 \tag{19}
\]
The maximum is attained. Its defining coefficients are only those
of the known quartic and original balls; \(w_*\) is not supplied
as input. With \(n=4Nq\), dense Gram blocks have size at most
\(\binom{n+2}{2}\) and \(n+1\), respectively.

For each fixed feasible trial \(u\), define the number
\[
 d(u)=F(u)-\tfrac12\|\nabla F(u)\|^2,\qquad
                         F(w)-d(u)\in Q_2(g).
 \tag{20}
\]
Complete the square in the linear and quadratic terms of (17).
It follows that
\[
 B_{\rm tot}^2\max(0,d(u))\le |K_N|^2
              \le\frac{197}{196}B_{\rm tot}^2F(u).
 \tag{21}
\]
Only the \(2q\) retained packets enter this gradient.
This is the inherited strong-convexity witness in genuinely
smaller coordinates, not a new geometric rate estimate.
For example, a family of retained trials with \(F(u_N)>0\) and
\[
 \eta_N=1-\frac{\|\nabla F(u_N)\|^2}{2F(u_N)}>0,\qquad
 \log\eta_N=o(N),\qquad
       \frac{\pi}{N}\log(B_{\rm tot}^2F(u_N))\longrightarrow V
\]
would give the original volume rate \(V\) by (21). Constructing
such geometric trials is still required.

## 5. Moment exactness and scope

The exact moment problem uses a functional \(\mathcal L\) through
degree four with
\[
 \mathcal L(1)=1,\quad
 \mathcal L(a^2)\ge0\ (\deg a\le2),\quad
 \mathcal L(g_i a^2)\ge0\ (\deg a\le1).
 \tag{22}
\]
Equation (19) gives \(\mathcal L(F)\ge m\); evaluation at \(w_*\)
attains equality. At any optimum,
\(\mathcal L(\|w-w_*\|^2)=0\).
The unit-ball localizers imply
\(0\le\mathcal L((w_a p)^2)\le\mathcal L(p^2)\) for linear
\(p\). Applied to each centered coordinate, they force
\(\mathcal L(((w_a-w_{*,a})w_b)^2)=0\).
Moment-matrix Cauchy--Schwarz then reduces every monomial through
degree four to its value at \(w_*\). Thus every optimal moment
functional is this evaluation, and its moment matrix has rank one.

If \(q=0\), all remaining interactions after the prescribed leaf
clamp are linear, and the original reduction already gives a
known constant minimum; the semidefinite statement is scalar.
The \(p=0\) single-chain case is likewise already evaluated.

The result proves degree-four exactness for this particular reduced
quartic on its original balls. It uses the exact small-chain
covariances and Hessian sum-of-squares identities, not convexity
alone. It preserves the same finite source and budget. It does not
make an exponentially small optimum easy to resolve, or construct
a geometric trial satisfying (21) at the volume rate. No new
knot-volume family or finite-exception theorem is asserted.

## Complete proof sources

All three complete matching texts were read:

| Source | SHA-256 |
|---|---|
| [Original Hessian and degree-four source certificate](research_conway_degree_four_semidefinite_certificate.md) | 8b706c7e08aa124ce5d80c2401511a3be67a09b1878b0adfd4ec989514cf44db |
| [Exact internal-edge covariances and root response](research_conway_binary_skeleton_quartic.md) | 294220039d913fd349b867f9705670215c3ca98f581461c6f406db0dac20c7a3 |
| [Branching reduction on the clamped source](research_conway_branching_quartic_source.md) | f62e3f9fbb1123ee6ad122a3624295172921d626efa9b97e39300ea1806cf2fb |

The branching reduction already preserves a quartic minimum. The
additional result is its exact degree-four certificate on the
smaller original ball domain, with its moment and trial consequences.
No generic polynomial-projection or convex-quartic assertion is used.

Only written mathematics and text/hash operations were used. No
mathematical program, numerical experiment, test, build, git operation
or earlier-final edit was performed.
