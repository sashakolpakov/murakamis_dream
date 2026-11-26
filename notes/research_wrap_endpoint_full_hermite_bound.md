# The complete wrap cap has a quadratic physical-jet bound

Private written research note, 16 November 2026.

The shifted factorial wrap coupon extends through its last endpoint in
the original full Hermite algebra. Its values are at most one, and
its first spectral normals are at most \(N^2/4\), uniformly over
the entire microscopic wrap cap and both level parities. The limiting
class is the original last Newton polynomial, up to the prescribed
period sign; its nonzero endpoint normal is essential.

This gives a source-preserving multiplier bound with arbitrary
spectators and the original closing functional retained. It is not
a uniform off-grid angular contour statement, a geometric-rate
comparison, or a lower bound for the closed scalar.

Polynomial control of the entire high half-period, including physical
first normals and the ordinary free-boundary polynomial, was already
proved in [the high-index boundary theorem](research_high_index_free_boundary_hermite_bound.md).
The present contribution is the explicit quadratic sharpening on the
real microscopic cap and the complete endpoint jets, nilpotent class,
and prescribed closing. It does not introduce a new domain of general
polynomial high-half control.

## 1. Physical classes and conventions

Put
\[
 N\ge2,\quad D=N-1,\quad \theta=\frac{\pi}{N},\quad
 \eta=(-1)^D,\quad P_N(z)=2T_N(z/2)+2,\quad
 \mathcal A_N=\mathbb C[z]/(P_N).
 \tag{1}
\]
Let
\[
 c_j=2\cos((2j+1)\theta),\qquad
 t_j=(D-2j)\theta,\qquad -2\cos t_j=c_j
                    \quad(0\le j\le D).
 \tag{2}
\]
The independent labels are \(0\le j\le m=\lfloor D/2\rfloor\).
When \(N\) is even all of these roots are double. When \(N\) is
odd, \(j=m\) gives the simple root \(c_m=-2,t_m=0\), and
the other independent roots are double. Labels \(j,D-j\)
describe the same spectral root.

Retain the actual canonical factorial and interpolation
\[
 B_N(x,t)=\frac{N}{
 G_N(D/2-Nx+Nt/(2\pi))
 G_N(D/2-Nx-Nt/(2\pi))G_N(Nx)^2}.
 \tag{3}
\]
For \(1/2\le s<1\), define the shifted full-Hermite class
\[
 V_{N,s}=[B_N(-s/N,t)]\in\mathcal A_N,\qquad z=-2\cos t.
 \tag{4}
\]
The exact internal Fourier-band theorem makes
\([B_N(x,t)]\) an entire function of \(x\) with values in
\(\mathcal A_N\). Accordingly (4) has a specified analytic
extension to \(s=1\); no endpoint value is assigned by an
arbitrary interpolation. The original wrap class is
\[
 Q_{N,s}=[B_N(1-s/N,t)]=\eta V_{N,s}.
 \tag{5}
\]
This equality includes every first normal, not merely values.

For \(f\in\mathcal A_N\), use the physical-jet norm
\[
 \|f\|_{\mathrm H}=
 \max\left\{
       \max_{c\text{ double}}\bigl(|f(c)|+|f'(c)|\bigr),
       \ |f(-2)|\ \text{if }N\text{ is odd}
      \right\}.
 \tag{6}
\]
The prime always denotes the derivative in the spectral variable
\(z\). The original closure is
\[
 \begin{split}
 \phi_N(f)
  &=\eta N^2\sum_{P_N(c)=0}
                   \operatorname{Res}_{z=c}\frac{f(z)\,dz}{P_N(z)}\\
  &=\eta\sum_{c\text{ double}}
        \bigl((4-c^2)f'(c)-cf(c)\bigr)
        +\mathbf1_{N\text{ odd}}f(-2).
 \end{split}
 \tag{7}
\]
Each distinct double root occurs once in this formula.

## 2. Exact values and normals

Write \(g_N'=G_N'/G_N\). For \(1/2\le s<1\), set
\[
 v_j(s)=\frac{G_N(j-s)}
                  {G_N(j+s)G_N(-s)^2},\qquad
 q_j(s)=g_N'(j+s)-g_N'(j-s).
 \tag{8}
\]
Then
\[
 V_{N,s}(c_j)=v_j(s),\qquad
 V_{N,s}'(c_j)=
       \frac{N\,v_j(s)q_j(s)}{4\pi\sin t_j}
                 \quad(c_j\text{ double}).
 \tag{9}
\]
The second formula is not imposed at the odd simple root.

To prove (8)--(9), substitute \(t_j\) into (3). The two
shifted factorial arguments become \(D+s-j\) and \(s+j\).
The exact reflection
\[
 G_N(z)G_N(D-z)=N,\qquad
                         g_N'(D-z)=g_N'(z)
 \tag{10}
\]
gives (8). Logarithmic differentiation of (3) in \(t\)
then gives \(Nv_jq_j/(2\pi)\). Division by
\(dz/dt=2\sin t_j\) proves (9). Reflection also gives
\[
 v_{D-j}(s)=v_j(s),\qquad q_{D-j}(s)=-q_j(s),
 \tag{11}
\]
so the duplicated physical labels have identical normals.

The label \(j=0\), which is the only singular-looking endpoint
of (8), has the explicit formulas
\[
 v_0(s)=\frac{\sin(\pi s)}{N\sin(\theta s)},\qquad
 q_0(s)=\theta\cot(\theta s)-\pi\cot(\pi s),
 \tag{12}
\]
\[
 V_{N,s}'(c_0)=
 \frac{v_0(s)}{4\sin\theta}
             \bigl(\cot(\theta s)-N\cot(\pi s)\bigr).
 \tag{13}
\]
Indeed recurrence and reflection imply
\[
 G_N(s)G_N(-s)=
                      \frac{N\sin(\theta s)}{\sin(\pi s)}.
 \tag{14}
\]
Taking a reciprocal and then a logarithmic derivative proves
(12); (13) is (9).

## 3. A bound uniform in every label and in the endpoint

**Theorem 1.** For every \(N\ge2\) and \(1/2\le s\le1\),
\[
 0\le V_{N,s}(c_j)\le1
                       \quad(0\le j\le m),
 \tag{15}
\]
and at every physical double root,
\[
 0\le V_{N,s}'(c_j)\le
 V_{N,s}'(c_0)\le
                  \frac{N}{2\sin\theta}\le\frac{N^2}{4}.
 \tag{16}
\]
Consequently
\[
 \|V_{N,s}\|_{\mathrm H}
       =\|Q_{N,s}\|_{\mathrm H}
                  \le C_N:=1+\frac{N^2}{4}.
 \tag{17}
\]

**Proof for \(s<1\).** The Gamma product is positive and
nonzero on the real defining interval \((-1,N)\).
Consequently every \(v_j\) in (8) is positive.
Recurrence gives
\[
 \frac{v_{j+1}(s)}{v_j(s)}
       =\frac{\sin\theta(j+1-s)}{\sin\theta(j+1+s)}.
 \tag{18}
\]
For \(0\le j<m\), both sines are positive and their denominator
minus numerator is
\(2\cos\theta(j+1)\sin(\theta s)>0\). Thus
\(v_j\le v_0\). Since \(\theta s\le\pi/2\),
\[
 N\sin(\theta s)\ge2s\ge1,
 \tag{19}
\]
and (12) proves \(v_0\le1\).

Logarithmic differentiation of the recurrence for \(G_N\) yields
\[
 \begin{split}
 q_{j+1}(s)-q_j(s)
 &=\theta\bigl(\cot\theta(j+1+s)-\cot\theta(j+1-s)\bigr)\\
 &=-\frac{\theta\sin(2\theta s)}
       {\sin\theta(j+1+s)\sin\theta(j+1-s)}<0
                    \qquad(0\le j<D).
 \end{split}
 \tag{20}
\]
All arguments in the denominator belong to \((0,\pi)\).
Together with (11), strict decrease gives \(q_j>0\) for
\(j<D/2\), and \(q_m=0\) at the odd simple root.
In particular \(0<q_j\le q_0\) at every independent double
root. Also
\[
                         \sin t_j\ge\sin\theta>0
 \tag{21}
\]
there. Equations (9), (18), (20), and (21) therefore give
the first two inequalities of (16).

To bound the last expression, use (12) to write
\[
 v_0q_0=
 \frac{\theta\sin(\pi s)\cos(\theta s)}
                          {N\sin^2(\theta s)}
 -\frac{\pi\cos(\pi s)}{N\sin(\theta s)}
 \le\frac{\pi}{4s^2}+\frac{\pi}{2s}\le2\pi.
 \tag{22}
\]
Here \(\sin(\theta s)\ge2\theta s/\pi\);
both terms on the displayed left are nonnegative because
\(s\in[1/2,1)\).
Formula (9) at \(j=0\) gives
\(V_{N,s}'(c_0)\le N/(2\sin\theta)\).
Finally \(\sin(\pi/N)\ge2/N\) proves (16).
The endpoint extension in the next section proves the same
inequalities at \(s=1\). \(\square\)

This bound is a statement about the literal spectral derivative,
with no level-dependent rescaling of its norm.

## 4. Every endpoint value and first normal

Let \(\epsilon=1-s\downarrow0\). Formula (12) gives
\[
 v_0(s)=\frac{\theta}{\sin\theta}\epsilon+O_N(\epsilon^2),
 \qquad
       \lim_{s\uparrow1}V_{N,s}'(c_0)
                            =\frac1{4\sin^2\theta}.
 \tag{23}
\]
The limit in (23) follows either from (13), or by observing that
\(v_0q_0\to\pi/(N\sin\theta)\). In particular the vanishing
value does not justify discarding the endpoint class.

For every independent label \(j\ge1\), recurrence gives
\[
 \frac1{G_N(-s)^2}
       =\frac{4\sin^2(\theta\epsilon)}{G_N(\epsilon)^2}
       =4\theta^2\epsilon^2+O_N(\epsilon^3).
 \tag{24}
\]
The other factorials in (8) are regular and nonzero at \(s=1\).
Hence
\[
 v_j(s)=
    \frac{\theta^2}
         {\sin(j\theta)\sin((j+1)\theta)}\epsilon^2
                          +O_N(\epsilon^3).
 \tag{25}
\]
This includes the odd simple root, whose value consequently
tends to zero. At every such double root,
\[
 V_{N,s}'(c_j)=
   \frac{\theta^2}
        {4\sin^2(j\theta)\sin^2((j+1)\theta)}\epsilon^2
                          +O_N(\epsilon^3).
 \tag{26}
\]
To check its coefficient, at \(s=1\)
\[
 q_j(1)=\theta\{\cot(j\theta)+\cot((j+1)\theta)\}
       =\frac{\theta\sin t_j}
                 {\sin(j\theta)\sin((j+1)\theta)}.
 \tag{27}
\]
Substitution in (9) gives (26). The remainders in
(23)--(26) are fixed-level endpoint expansions; the
uniform-in-level assertion is (15)--(17).

Thus \(V_{N,1}\) has value zero at every physical root,
first normal \(1/(4\sin^2\theta)\) at \(c_0\), and first
normal zero at every other double root. These statements
also cover \(N=2\), when \(c_0=0\) is the only root and
the normal is \(1/4\).

Let \(e_D\) be the original last Newton polynomial. Since
\(c_D=c_0\) and \(S_D=\prod_{\ell=1}^D2\sin(\ell\theta)=N\),
\[
 e_D(z)=\frac{\eta P_N(z)}{N^2(z-c_0)}.
 \tag{28}
\]
Its only nonzero physical jet is
\(e_D'(c_0)=\eta/(4\sin^2\theta)\). This follows from
the Chebyshev double-root identity
\(P_N(z)/(z-c_0)^2|_{z=c_0}=N^2/(4-c_0^2)\).
The endpoint data above therefore prove
\[
             V_{N,1}=\eta e_D,\qquad Q_{N,1}=e_D.
 \tag{29}
\]
They agree with the analytic class continuation in Section 1.
In particular
\[
 V_{N,1}^2=Q_{N,1}^2=0,\qquad
 \phi_N(V_{N,1}A)=\eta A(c_0),\qquad
 \phi_N(Q_{N,1}A)=A(c_0)
                         \quad(A\in\mathcal A_N).
 \tag{30}
\]
These formulas retain the original \(\eta N^2\) trace
normalization. Nilpotence follows either from the displayed
jets or from \(P_N\mid e_D^2\). The trace identities follow
by inserting those same jets in (7).

## 5. Original spectators, several vertices, and norm scope

The norm (6) is submultiplicative by the product rule:
\[
       \|AB\|_{\mathrm H}\le\|A\|_{\mathrm H}\|B\|_{\mathrm H}.
 \tag{31}
\]
The exact closure (7) also gives
\[
                         |\phi_N(A)|\le3N\|A\|_{\mathrm H}.
 \tag{32}
\]
Indeed each double-root term is at most
\(4(|A|+|A'|)\), there are at most \(N/2\) such roots,
and there is at most one simple-root term.

For arbitrary \(A\in\mathcal A_N\) and any fixed number \(k\)
of wrap factors, (5), (17), and (31)--(32) give
\[
 \begin{split}
 \phi_N\left(A\prod_{\nu=1}^kQ_{N,s_\nu}\right)
    &=\eta^k\phi_N\left(A\prod_{\nu=1}^kV_{N,s_\nu}\right),\\
 \left|\phi_N\left(A\prod_{\nu=1}^kQ_{N,s_\nu}\right)\right|
    &\le3N C_N^k\|A\|_{\mathrm H},
                   \qquad \tfrac12\le s_\nu\le1.
 \end{split}
 \tag{33}
\]
The spectator may contain any original signed crossing powers,
attached kernels, and outside boundary coefficients. Its
growth remains the explicit factor \(\|A\|_{\mathrm H}\).
An even holomorphic angular spectator near the physical grid
defines the same kind of class, including its original
crossing-Gaussian full jets, so (33) applies without replacing
that class by only its nodal values.

There is an identical tensor statement. At \(r\) traced
vertices, define the mixed Hermite norm by taking the maximum,
over assignments of one distinct-root label to each vertex, of
\[
        \sum_{J\subset D_{\rm dbl}}|\partial_J A|,
 \tag{34}
\]
where repetitions of a root at different vertices are allowed,
and \(D_{\rm dbl}\) is the set of coordinates assigned a
double root; each coordinate is differentiated at most once.
This norm is submultiplicative. The original tensor closure
has norm at most \((3N)^r\). If \(k\) is the total number of
replaced traced halfwires, then the full contraction obeys
\[
 \left|\phi_N^{\otimes r}
       \left(A\prod_{\nu=1}^k Q_{N,s_\nu}(z_{v_\nu})\right)\right|
       \le (3N)^r C_N^k\|A\|_{\mathrm H,r}.
 \tag{35}
\]
The equality preceding the bound again carries the exact
factor \(\eta^k\). Ordinary free cardinal factors are retained
in \(A\); no quotient or estimate at those free arguments is
inserted. The identities also commute with every retained
outside derivative. Equations (33)--(35) may be integrated
over the real wrap parameters, including the whole cap
\(s\in[1/2,1]\), since the bounds are uniform there.

The analytic representative \(B_N(-s/N,t)\) does not have a
common full-grid angular neighborhood as \(s\uparrow1\).
At a generic fixed off-grid angle its limit is zero, whereas
the limiting physical class (29) is nonzero and nilpotent.
The missing information lies at the moving endpoint normal.
Consequently Theorem 1 is a full-source jet and multiplier
bound, not an extension of the earlier full-grid angular
rectangle theorem through its pinching endpoint.

In particular (35) does not bound the remaining spectator
at the positive geometric action, and supplies no surviving
geometric coefficient. It controls the complete microscopic
wrap cap at polynomial cost while preserving the prescribed
closing.

## 6. Direct written source versions

All directly used source implications were checked in the
following full written versions. Their hashes are pinned.

- [Canonical factorial and exact finite derivative](research_exact_cyclotomic_factorial.md):
  SHA-256 0f989261f53747266ac62dba40ca7548138012b266521e98a03bd94b450c657b.
- [Full-Hermite entire Fourier band and circle averaging](research_internal_wire_exact_circle_averaging.md):
  SHA-256 0efa85a43da064197f25422d86ef37688971f2dface55da9d5efef3ccb0d08ef.
- [Wrap factorization and its angular-domain scope](research_factorial_wire_wrap_obstruction.md):
  SHA-256 c70141bf826dced9945f431f6d9f0a27076fe155f7ef3dd1ddd9143e0afb9341.
- [Original residue normalization and last-Newton class](research_actual_source_dualizing_residue.md):
  SHA-256 806f8e4530736632830a15cff19f4c0f72e659fa6280d48005c4184a6ffc9afb.
- [Prior full high-half and ordinary free-boundary bound](research_high_index_free_boundary_hermite_bound.md):
  SHA-256 041ba93916ffb71d5549286538c24302d89f80b0f1936ea928f6dd3eaf490ac7.

No mathematical code, tests, or numerical evidence are used.
