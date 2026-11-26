# The full edge-kernel difference equation and its endpoint normal

Research note, 3 November 2026.

The physical rows of the original edge kernel satisfy a standard
Askey--Wilson recurrence. The full finite kernel has an additional
term off the physical spectrum. We compute that term exactly,
including its first normals, and prove a sharp bound for every
entry in the endpoint row of its mixed logarithmic derivative.

These identities concern the original polynomial kernel. They do
not replace the coherent spectral sum by its absolute value.
The companion [all-color theorem](research_all_color_path_normal_bound.md)
now proves the needed one-sided bound at every pair of physical
double roots, using the full normal equation established here.

## 1. The finite kernel and the difference operator

Fix \(N\ge2\), and set
\[
 \theta=\pi/N,\quad D=N-1,\quad \eta=(-1)^D,\qquad
 s_x=2\sin(x\theta),\quad c(x)=2\cos((2x+1)\theta),
 \quad c_j=c(j),\quad c_0=2\cos\theta.
 \tag{1}
\]
The subscript \(x\) in \(s_x\) may be complex. Let
\[
 S_i=\prod_{r=1}^{i}s_r,\qquad
 e_i(z)=S_i^{-2}\prod_{r=0}^{i-1}(c_r-z),\qquad
 K_N(z,w)=\sum_{i=0}^{D}e_i(z)e_i(w).
 \tag{2}
\]
The physical relation, in standard Chebyshev notation, is
\[
 P_N(z)=2T_N(z/2)+2,\qquad
                 (z-c_0)e_D(z)=\frac{\eta}{N^2}P_N(z).
 \tag{3}
\]
The sign in (3) is fixed by the leading coefficient
\([z^D]e_D=\eta/N^2\).

For meromorphic functions of \(x\), define
\[
 \begin{split}
 A(x)&=\frac{s_{x+1}^{\,4}}{s_{2x+1}s_{2x+2}},&
 C(x)&=\frac{s_x^{\,4}}{s_{2x}s_{2x+1}},\\
 (\mathcal L f)(x)&=-A(x)f(x+1)
       +(c_0+A(x)+C(x))f(x)-C(x)f(x-1).
 \end{split}
 \tag{4}
\]
Expressions at apparent poles are interpreted by continuation.
The calculation below proves that \(\mathcal L\) maps every
polynomial in \(c(x)\) of degree at most \(D\) to another such
polynomial. Thus its combined expression has removable
singularities there, even when its separate terms do not.

**Theorem 1.** The exact finite kernel satisfies
\[
 \boxed{\displaystyle
 wK_N(c(x),w)-\mathcal L_xK_N(c(x),w)
    =(w-c_0)e_D(c(x))e_D(w)
    =\frac{\eta}{N^2}P_N(w)e_D(c(x)).}
 \tag{5}
\]
This is an ordinary polynomial identity in the second variable
and an analytically continued identity in the first.

*Proof.* Put \(E_i(x)=e_i(c(x))\). Sine subtraction gives
\[
 E_i(x)=\prod_{r=0}^{i-1}
              \frac{s_{x+r+1}s_{x-r}}{s_{r+1}^2}.
 \tag{6}
\]
At points where the divisions are allowed,
\[
 \frac{E_i(x+1)}{E_i(x)}
       =\frac{s_{x+i+1}}{s_{x-i+1}},\quad
 \frac{E_i(x-1)}{E_i(x)}
       =\frac{s_{x-i}}{s_{x+i}},\quad
 \frac{E_{i-1}(x)}{E_i(x)}
       =\frac{s_i^2}{s_{x+i}s_{x-i+1}}.
 \tag{7}
\]
Substitution in (4), followed by sine addition, proves
\[
 \mathcal L E_0=c_0E_0,\qquad
 \mathcal L E_i=c_iE_i-s_i^2E_{i-1}\quad(1\le i\le D).
 \tag{8}
\]
One can verify this last algebraic step without branch choices.
Put \(q=e^{\mathrm i\theta}\), \(X=e^{2\mathrm i x\theta}\),
and \(V=q^{2i}\), where \(i\) is the integer Newton index.
The two coefficients in (4) become
\[
 A=-\frac{(q^2X-1)^4}
            {q(q^2X^2-1)(q^4X^2-1)},\qquad
 C=-\frac{q(X-1)^4}{(X^2-1)(q^2X^2-1)}.
 \tag{9}
\]
The identity required by (8) is precisely
\[
 \begin{split}
 q+q^{-1}+A+C
 &-A\frac{q^2XV-1}{q^2X-V}
  -C\frac{X-V}{XV-1}\\
 &=qV+q^{-1}V^{-1}
   +\frac{qX(V-1)^4}{V(XV-1)(q^2X-V)}.
 \end{split}
 \tag{10}
\]
Clearing its displayed denominators gives the zero polynomial.
This also proves (8) at zeros of \(E_i\), by continuation.

Finally \(we_i(w)=c_i e_i(w)-s_{i+1}^2e_{i+1}(w)\)
for \(i<D\). Apply this relation to the sum (2).
The coefficients through \(e_{D-1}(w)\) match (8).
The last coefficient leaves exactly
\((w-c_D)e_D(c(x))e_D(w)\), where \(c_D=c_0\).
Equation (3) gives the last form of (5). \(\square\)

In particular, (5) vanishes in the full physical quotient in
\(w\), including every first normal at a double root. It
does not vanish as an ordinary free-boundary polynomial.
The distinction is explicit, rather than an omitted
endpoint condition.

## 2. Physical rows and coalescing shifts

For \(0\le j\le\lfloor D/2\rfloor\), the distinct physical
row is
\[
 F_j(w):=K_N(c_j,w)
     =\sum_{i=0}^{j}\frac{S_{j+i}}{S_{j-i}S_i^2}e_i(w).
 \tag{11}
\]
Thus it has degree exactly \(j\), and \(F_j(c_0)=1\).
Its recurrence, wherever the separate coefficients are
finite, is
\[
 wF_j=-A_jF_{j+1}+(c_0+A_j+C_j)F_j-C_jF_{j-1},
 \quad A_j=A(j),\ C_j=C(j),\ C_0=0.
 \tag{12}
\]
It follows directly from (5), since \(e_D(c_j)=0\).

This is the normalized Askey--Wilson recurrence. In the
notation of [DLMF (18.28.1_5)](https://dlmf.nist.gov/18.28.E1_5)
and [(18.28.6_3)--(18.28.6_4)](https://dlmf.nist.gov/18.28),
the parameters are \(a=b=c=d=q=e^{i\theta}\), the base is
\(Q=q^2\), and the polynomial variable satisfies
\(Z+Z^{-1}=w\). Its two recurrence coefficients are
\(-A_j,-C_j\). The terminating rational identities continue
to the present root of unity whenever their denominators
are nonzero. No positive orthogonality measure at this
complex base is being imported.

Root-of-unity Askey--Wilson orthogonality is treated by
[Spiridonov and Zhedanov, Duke Math. J. 89 (1997), 283--305](https://arxiv.org/abs/q-alg/9605034).
Their general finite orthogonality theorem assumes a simple
spectral grid and excludes parameter products that are powers
of the base; see their conditions (2.8)--(2.9).
The present parameters and repeated physical roots are a
degenerate specialization of those conditions. Thus that
theorem does not remove the confluence or the original
normal term in (5).

For \(j\ge1\) in (11), all \(A_r>0\) for \(0\le r<j\)
and \(C_r>0\) for \(1\le r<j\). The leading \(j\)-by-\(j\)
Jacobi matrix of (12) is symmetrizable and has all
eigenvalues strictly larger than \(c_0\).
Indeed choose \(\pi_0=1\) and
\(\pi_{r+1}C_{r+1}=\pi_rA_r\).
Its quadratic form after subtracting \(c_0\) is
\[
       \sum_{r=0}^{j-1}\pi_r A_r|v_r-v_{r+1}|^2,
                  \qquad v_j=0.
 \tag{13}
\]
It is positive definite, and the off-diagonal entries are
nonzero. Its eigenvalues, hence the roots of \(F_j\),
are real and simple. This argument proves a lower bound
by \(c_0\); it does not claim a lower bound by \(2\).

At the middle of the original spectral list, separate
coefficients in (12) can have poles and shifted spectral
points coalesce. For example, when \(N=2m\) and \(j=m-1\),
\(A(j)\) has a pole while \(c(j+1)=c(j)\). Substituting
only these coincident values into (12) would lose a first
normal. The correct equation is the limit of (5), or,
equivalently, the polynomial operator (8).

The source in (5) also identifies the exceptional endpoint
normal. At a double root other than \(c_0\),
\(e_D(c_j)=e_D'(c_j)=0\). At \(c_0\),
\[
                          e_D'(c_0)=\frac{\eta}{s_1^2}.
 \tag{14}
\]
Differentiating (5) in its spectral first variable thus
leaves the defect \(P_N(w)/(N^2s_1^2)\) at \(c_0\).
This is the original first-normal endpoint, not an
arbitrary choice of a recurrence boundary condition.

## 3. The sharp endpoint-row inequality

At physical root pairs \(K_N(c_j,c_k)>0\),
because all surviving coefficients in (11) are positive.
Define the real mixed logarithmic derivative
\[
 H_{jk}=
 \left.\partial_z\partial_w\log K_N(z,w)
                                      \right|_{(c_j,c_k)}.
 \tag{15}
\]
We consider double roots in the following bound. Put
\[
 \tau_j=\pi-(2j+1)\theta,\quad
 m_j=N-2j-1>0,\quad
 \gamma_j=\frac{N\tau_j}{4\pi\sin\tau_j}
          =\frac{m_j}{4\sin((2j+1)\theta)}.
 \tag{16}
\]
The factor \(\gamma_j\) is the exact angular-to-spectral
normal of a unit original crossing:
\((R^n)'(c_j)/R^n(c_j)=in\gamma_j\).

**Theorem 2.** Every double physical root satisfies
\[
 \boxed{\displaystyle
 H_{0j}
   =\frac{\displaystyle\sum_{r=j+1}^{N-1-j}
                              \csc^2(r\theta)}
          {16\sin\theta\sin((2j+1)\theta)},\qquad
 0<H_{0j}\le
       \frac{N+1}{3(N-1)}\,\gamma_0\gamma_j.}
 \tag{17}
\]
Equality in the bound holds at \(j=0\).

*Proof.* Let \(\Pi_0\) be the full local idempotent at the
double root \(c_0\). The original kernel identities are
\[
 K_N(c_0,w)=1,\qquad
 \partial_z K_N(c_0,w)
    =\frac{\eta T\Pi_0(w)+c_0}{s_1^2}.
 \tag{18}
\]
The exact first normal of the Ward coupon, proved in
[the signed Gaussian packet calculation](research_signed_gaussian_ward_endpoint_packet.md),
is
\[
 (T\Pi_0)'(c_j)=
 \frac{(-1)^{N+1}\sin\theta}
      {4\sin((2j+1)\theta)}
       \sum_{r=j+1}^{N-1-j}\csc^2(r\theta).
 \tag{19}
\]
Since \(\eta=(-1)^{N+1}\), differentiating (18) proves
the equality in (17). In particular, it includes all
high-index first normals in the original polynomial.

The remaining finite inequality is elementary. The sequence
\(\csc^2(r\theta)\), \(1\le r<N\), is symmetric and
decreases towards its center. Removing equal numbers of
its two outside entries cannot increase its mean.
The retained interval in (17) has \(m_j\) entries, and
\[
 \sum_{r=1}^{N-1}\csc^2(r\theta)=\frac{N^2-1}{3}.
 \tag{20}
\]
Therefore its sum is at most \(m_j(N+1)/3\).
Dividing the exact expression by
\(\gamma_0\gamma_j=(N-1)m_j/
 [16\sin\theta\sin((2j+1)\theta)]\)
proves the bound. All summands are positive. \(\square\)

## 4. A consequence for the full first-normal determinant

The colored determinant in
[the grouped-current calculation](research_grouped_endpoint_current_matchings.md),
equations (14)--(17), can be symmetrized after its
crossing values and \(4-c_j^2\) are factored out.
At double physical nodes its diagonal is a real number
plus \(in_v\gamma_{j_v}\). For an edge with \(H_{jk}\ge0\),
take its two symmetric off-diagonal entries to be
\(i\sqrt{H_{jk}}\). The transposition term in the determinant
then has the required positive sign. Thus the imaginary
part is a real symmetric matrix.

For a finite path, suppose \(|n_v|\ge2\) with one common
sign, and every edge has at least one endpoint assigned
the physical value \(c_0\). Normalize by the diagonal
matrix with entries \(\sqrt{\gamma_{j_v}}\).
Theorem 2 bounds the absolute off-diagonal entries of
the normalized imaginary part by
\[
                 \sqrt{\frac{N+1}{3(N-1)}}\le1.
 \tag{21}
\]
Its diagonal entries have the common sign and magnitude
at least \(2\). The tridiagonal matrix with diagonal
\(2\) and off-diagonal entries \(-1\) is positive definite
on every finite path: its quadratic form is a sum of
squared successive differences and the two endpoint
squares. Replacing each off-diagonal entry by one of
smaller absolute value preserves the same strict bound
by the triangle inequality.
Consequently this colored first-normal determinant is
nonzero. The argument also applies to the double-root
components remaining after odd simple roots are evaluated.

There is a quantitative version. Let \(m\ge1\) be the number
of remaining double-root vertices and put
\[
                    \lambda_m=2-2\cos\frac{\pi}{m+1}>0.
 \tag{22}
\]
After choosing the common sign, the imaginary part \(B\)
of the normalized symmetric determinant matrix satisfies
\[
           B\ge\lambda_m\operatorname{diag}(\gamma_{j_v}).
 \tag{23}
\]
The same bound holds for a disjoint union of subpaths with
at most \(m\) vertices. If the real symmetric part is \(A\),
conjugating by \(B^{-1/2}\) gives
\[
 |\det(A+iB)|=\det B\,
   \left|\det(B^{-1/2}AB^{-1/2}+iI)\right|
                    \ge\det B.
 \tag{24}
\]
The last inequality follows because the eigenvalues of the
real symmetric middle matrix are real, and
\(|x+i|\ge1\). Since \(\tau/\sin\tau\ge1\),
\[
              |\det(A+iB)|
                    \ge\left(\frac{N\lambda_m}{4\pi}\right)^m.
 \tag{25}
\]
For the original scalar path whose spectators are its
remaining edge kernels, each removed row factor has
absolute value \(4-c_j^2\ge16/N^2\); the crossing values
have modulus one. Also \(F(\mathbf c)\ge1\).
Restoring these factors therefore gives the explicit lower
bound
\[
       |\text{contribution of the covered color assignment}|
                       \ge\left(\frac{4\lambda_m}{\pi N}\right)^m.
 \tag{26}
\]
An odd simple-root evaluation has a unit crossing value and
introduces no derivative row. When there are no double-root
vertices, the kernel product directly gives a lower bound
of one. Thus the covered assignments lose at most a
polynomial factor at each fixed path length.

This verifies a family of complete spectral assignments,
not merely a one-vertex normal. The
[all-color extension](research_all_color_path_normal_bound.md)
now also handles edges joining two interior double roots.
It proves the one-sided bound \(H_{jk}\le\gamma_j\gamma_k\).
Neither \(H_{jk}\ge0\) nor the sharper two-sided estimate
\(|H_{jk}|\le\gamma_j\gamma_k\) is asserted.
For the determinant conclusion, the one-sided bound suffices: when
\(H_{jk}<0\), use the real symmetric off-diagonal entry
\(\sqrt{-H_{jk}}\). Its determinant contribution is still
\(H_{jk}\), while it contributes nothing to the imaginary
part. The same tridiagonal comparison then applies.
These bounds control the determinant at one
color assignment, not the coherent sum over assignments.
The crossing phases in that sum still have to be retained.

## 5. Reproduction

Run
~~~sh
python3 experiments/check_edge_kernel_difference_and_endpoint_bound.py \
  --precision 100 \
  --output repro/results/research-edge-kernel-difference-and-endpoint-bound.json
~~~
The [standalone script](../experiments/check_edge_kernel_difference_and_endpoint_bound.py)
first clears the rational identity (10) symbolically. It then
uses the defining Newton recurrence, retaining every index
through \(D\), to check (5) and its free-boundary derivative
at 44 nonphysical complex argument pairs over \(N=2,\ldots,12\).
It separately checks (17) at 144 double-root pairs over
\(N=2,\ldots,24\).
The [saved record](../repro/results/research-edge-kernel-difference-and-endpoint-bound.json)
passed at 100 decimal digits, with largest relative discrepancy
\(8.78\cdot10^{-97}\). These computations check the exact
normalization; they do not test or prove the missing
interior--interior inequality.

A [140-digit replay](../repro/results/research-edge-kernel-difference-and-endpoint-bound-root.json)
checks the same symbolic identity, 44 full-kernel cases and 144
endpoint pairs. Its largest relative discrepancy is
\(1.07\cdot10^{-136}\) or smaller.
