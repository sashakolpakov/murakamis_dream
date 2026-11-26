# Exact finite-band unit-turn conjugation and the branching forcing

Private written proof, 16 November 2026.

Conjugating spectral multiplication by an original unit turn gives
an explicit tridiagonal operator. A fixed number of turns therefore
preserves a finite-band operator presentation, with polynomial
operator cost for the conjugated multiplication itself. This is not
a polynomial bound for the turn operator. The ordinary branching
product has an additional mixed-difference forcing, retained below
with its original full normal data. Its growth after turning remains
uncontrolled by the present calculation.

## 1. Original operators and the conjugation formula

Put
\[
 N\ge2,\quad D=N-1,\quad q=e^{\pi i/N},\quad
 \eta=(-1)^D,\quad \kappa=q^{D^2/2},
\]
\[
 s_j=2\sin(j\pi/N),\quad S_j=\prod_{h=1}^j s_h,\quad S_0=1,
 \qquad c_j=q^{2j+1}+q^{-2j-1},
\]
\[
 P_N(Z)=2T_N(Z/2)+2,\qquad
 e_j(Z)=S_j^{-2}\prod_{h<j}(c_h-Z),\qquad
 \mathcal A_N=\mathbb C[Z]/(P_N).
 \tag{1}
\]
Here \(T_N\) in \(P_N\) is the usual Chebyshev polynomial.
The physical turn is denoted \(T\), so \(Te_j=e_{D-j}\).
The original kernel and Frobenius functional are
\[
 K_N(w,Z)=\sum_{j=0}^{D}e_j(w)e_j(Z),\qquad
 \phi_N(e_i e_j)=\mathbf1_{i+j=D}.
\]
Retain the original crossing \(R\), all its carriers, and
\[
 C f=Zf\pmod{P_N},\qquad J=TCT,\qquad
 U_\sigma=\kappa^\sigma TR^{-\sigma}T,\quad \sigma=\pm1.
 \tag{2}
\]
Every algebra element below has its ordinary canonical
representative of degree at most \(D\). In this basis,
\[
 Ce_j=c_je_j-s_{j+1}^2e_{j+1},\qquad
 Je_j=c_je_j-s_j^2e_{j-1},                              \tag{3}
\]
with out-of-range terms zero. In particular the raising term
at \(j=D\) is zero in the full algebra.

**Theorem 1.** For \(N\ge3\),
\[
 \boxed{\quad
 U_\sigma C U_\sigma^{-1}
  =\frac8{c_0}I+
      \frac{q^{-\sigma}JC-q^\sigma CJ}
           {q^{2\sigma}-q^{-2\sigma}} .
 \quad}                                                   \tag{4}
\]
Its full Newton action, valid also at \(N=2\), is
\[
 U_\sigma C U_\sigma^{-1}e_j
  =q^{-2\sigma j}s_j^2e_{j-1}
       +d_{\sigma,j}e_j
       +q^{-2\sigma(j+1)}s_{j+1}^2e_{j+1},
\]
\[
 d_{\sigma,j}
   =4q^{-\sigma(2j+1)}
       -(q^{-\sigma}+q^{-3\sigma})q^{-4\sigma j}.
 \tag{5}
\]
Thus (4) is an identity of the original nonsemisimple algebra's
linear operators. It includes every physical first normal.

### Complete entry verification

It suffices first to prove (5) for \(\sigma=1\).
Write \(U=U_+\) and let \(D_+\) be the tridiagonal matrix in (5).
The full triangular matrix from the exact unit-turn source is
\[
 U_{rj}=(-1)^j q^{-j(r+1)}
                  \frac{S_j}{S_rS_{j-r}}\quad(0\le r\le j\le D),
 \qquad U_{rj}=0\quad(r>j).
 \tag{6}
\]
We prove \(D_+U=UC\), including the ends of the matrix.
For \(0\le r\le j<D\), the ratios used in that comparison are
\[
 \frac{U_{r,j+1}}{U_{rj}}
       =-q^{-r-1}\frac{s_{j+1}}{s_{j-r+1}},\qquad
 \frac{U_{r-1,j}}{U_{rj}}
       =q^j\frac{s_r}{s_{j-r+1}},\qquad
 \frac{U_{r+1,j}}{U_{rj}}
       =q^{-j}\frac{s_{j-r}}{s_{r+1}}.
 \tag{7}
\]
The absent lower or upper ratios at \(r=0\) or \(r=j\)
are interpreted by their displayed zero numerators.
After clearing \(s_{j-r+1}\), the required identity is
\[
 \begin{split}
 0={}&(c_j-d_{+,r})s_{j-r+1}
       +q^{-r-1}s_{j+1}^3-q^{j-2r}s_r^3\\
    &-q^{-j-2r-2}s_{r+1}s_{j-r}s_{j-r+1}.
 \end{split}                                             \tag{8}
\]
Here is a direct Laurent verification. Substitute
\(x=q^r,z=q^{j-r}\), and use \(s_\ell=(q^\ell-q^{-\ell})/i\).
After multiplying (8) by \(i^3\), only powers
\(z^3,z,z^{-1},z^{-3}\) remain. Their coefficients are,
respectively,
\[
 0,\qquad
 qd_{+,r}-4x^{-2}+(1+q^{-2})x^{-4},
\]
\[
 4q^{-2}x^{-2}-q^{-1}d_{+,r}
                 -(q^{-2}+q^{-4})x^{-4},\qquad 0.
 \tag{9}
\]
Both middle coefficients vanish by (5). This verifies every
entry in this range, rather than only the first off-diagonal.

The entry \(r=j+1\) compares
\(-s_{j+1}^2U_{j+1,j+1}\) with
\(q^{-2j-2}s_{j+1}^2U_{jj}\); they agree directly by (6).
Entries \(r>j+1\) are zero on both sides.
For \(j=D,r>0\), the same cleared identity (8) applies with
\(s_{j+1}=s_N=0\), while \(s_{N-r}\ne0\).
The only division excluded from that argument is \(r=0,j=D\).
At this corner \(q^{-D}=-q\), \(s_D=s_1\), and
\[
 \frac{U_{1D}}{U_{0D}}=q^{-D}.
\]
The right side divided by \(U_{0D}\) is therefore
\[
 d_{+,0}+q^{-D-2}s_1^2
      =d_{+,0}-q^{-1}s_1^2=c_0,
 \tag{10}
\]
as required. This proves \(D_+U=UC\) throughout the finite matrix.
Since the diagonal entries of \(U\) are nonzero, (5) follows.

To identify (4), compute \(q^{-1}JC-qCJ\) using (3).
Its off-diagonal entries divided by \(q^2-q^{-2}\) are precisely
those of (5). Its diagonal at \(j\) is
\[
 (q^{-1}-q)c_j^2+q^{-1}s_{j+1}^4-qs_j^4
   =(q^2-q^{-2})d_{+,j}-8(q-q^{-1}).
 \tag{11}
\]
Since \(q^2-q^{-2}=(q-q^{-1})c_0\), adding \(8I/c_0\)
gives the claimed diagonal. Both denominators in (4) are
nonzero for \(N\ge3\).
Coefficient conjugation in the real Newton basis proves the
negative-sign formula with exactly its displayed phases.

For \(N=2\), formula (4) is undefined and is not used.
In the ordered basis \((e_0,e_1)\),
\[
 U_\sigma=\begin{pmatrix}1&i\sigma\\0&1\end{pmatrix},
 \qquad C=\begin{pmatrix}0&0\\-4&0\end{pmatrix},
\]
\[
 U_\sigma C U_\sigma^{-1}
   =\begin{pmatrix}-4i\sigma&-4\\-4&4i\sigma\end{pmatrix}.
 \tag{12}
\]
This is also (5), with its zero end terms. The proof is complete.

### The cyclic identities, including the shortest level

Put \(\mathsf X=C,\mathsf Y=J,\mathsf Z=D_+\), and
\(\Delta=q^2-q^{-2}\). The three identities have a
denominator-free form valid for every \(N\ge2\):
\[
 \boxed{\begin{split}
 q\mathsf X\mathsf Y-q^{-1}\mathsf Y\mathsf X
       &=8(q-q^{-1})I-\Delta\mathsf Z,\\
 q\mathsf Y\mathsf Z-q^{-1}\mathsf Z\mathsf Y
       &=8(q-q^{-1})I-\Delta\mathsf X,\\
 q\mathsf Z\mathsf X-q^{-1}\mathsf X\mathsf Z
       &=8(q-q^{-1})I-\Delta\mathsf Y.
 \end{split}}                                             \tag{12a}
\]
For \(N\ge3\), the first is (4). Here is a full entry check
of the second. In \(qJD_+-q^{-1}D_+J\), the shift \(+1\)
coefficient is \(\Delta s_{j+1}^2\). The shift \(-2\)
coefficient cancels exactly. The shift \(-1\) coefficient is
\[
 s_j^2\{\Delta q^{-4j}-qd_{+,j}+q^{-1}d_{+,j-1}\}=0.
 \tag{12b}
\]
At \(j=0\) this is an absent term, so \(d_{+,-1}\) is
not required. The diagonal coefficient is
\[
 (q-q^{-1})c_jd_{+,j}
       +q^{-2j-1}(s_j^4-s_{j+1}^4)
       =8(q-q^{-1})-\Delta c_j.                            \tag{12c}
\]
Both equalities follow directly on substituting (5);
for (12c), expand \(s_j^4=q^{4j}+q^{-4j}
-4q^{2j}-4q^{-2j}+6\).
Zero end factors \(s_0=s_N=0\) retain the same identities
at the first and last columns. These are all possible bands,
so the second relation follows. Since \(J=C^{\mathsf T}\)
and \(D_+=D_+^{\mathsf T}\) in the Newton coordinates,
transposition proves the third. At \(N=2\), the matrices
in (12), together with \(J=C^{\mathsf T}\), give all three
relations directly: \(\Delta=0\) and the scalar is \(16i\).
Thus no division by \(c_0\) or \(\Delta\) is hidden at that level.
Complex conjugation gives the corresponding signed presentation
for \(D_-\). No classical curve or knot invariant is identified
by these operator identities alone.

### The exact central relation

The same operators satisfy the quantum cubic
\[
 \boxed{\begin{split}
 &q\mathsf X\mathsf Y\mathsf Z
   +q^2\mathsf X^2+q^{-2}\mathsf Y^2+q^2\mathsf Z^2\\
 &\hspace{6mm}-8q\mathsf X-8q^{-1}\mathsf Y-8q\mathsf Z
       =(c_0^2-32)I .
 \end{split}}                                             \tag{12d}
\]
Here too \(N=2\) is included. For a full algebraic proof, denote
the left side by \(\Omega\), and put \(k=8(q-q^{-1})\).
Successive use of (12a), without division, gives
\[
 \begin{split}
 q[\mathsf X\mathsf Y\mathsf Z,\mathsf X]
    &=k\mathsf X(\mathsf Y-\mathsf Z)
       +\Delta\mathsf X(\mathsf Z^2-\mathsf Y^2),\\
 q^{-2}[\mathsf Y^2,\mathsf X]+q^2[\mathsf Z^2,\mathsf X]
    &=\Delta\mathsf X(\mathsf Y^2-\mathsf Z^2)
       +kc_0(\mathsf Z-\mathsf Y),\\
 [-8q^{-1}\mathsf Y-8q\mathsf Z,\mathsf X]
    &=k\mathsf X(\mathsf Z-\mathsf Y)
       +8\Delta(\mathsf Y-\mathsf Z).
 \end{split}                                             \tag{12e}
\]
Since \(kc_0=8\Delta\), these identities prove
\([\Omega,\mathsf X]=0\).
They can be checked by moving each rightmost \(\mathsf X\)
left using respectively the third and first equations of (12a);
all terms are displayed in (12e), including the scalar terms.
Likewise,
\[
 q(\mathsf Y\mathsf Z\mathsf X-\mathsf X\mathsf Y\mathsf Z)
     =k(\mathsf Y-\mathsf Z)
        +\Delta(\mathsf Z^2-\mathsf Y^2).                  \tag{12f}
\]
Consequently the expression defining \(\Omega\) is unchanged
under the cyclic substitution
\((\mathsf X,\mathsf Y,\mathsf Z)\mapsto
(\mathsf Y,\mathsf Z,\mathsf X)\). Thus it commutes with
\(\mathsf Y\) and \(\mathsf Z\) as well.

The eigenspace \(\ker(J-c_0)\) is \(\mathbb C e_0\).
Indeed, the only diagonal occurrences of \(c_0\) in (3) are
at \(j=0,D\). Every intermediate diagonal differs from \(c_0\),
and all the upper links \(-s_j^2\), \(1\le j\le D\), are nonzero.
Solving the triangular equations from the last row through
the first forces every coefficient except that of \(e_0\)
to vanish; this also applies directly when \(N=2\).
Since \(\Omega\) commutes with \(J\), it sends \(e_0\)
to a scalar multiple of \(e_0\). The vector \(e_0\) is cyclic
for \(C\), because all its successive raising links in (3)
are nonzero. Commutation with \(C\) now makes \(\Omega\) scalar
on the whole algebra.

To evaluate the scalar, put
\(h=q-q^{-1}\) and \(d_0=3q^{-1}-q^{-3}\).
The coefficient of \(e_0\) in \(\Omega e_0\) is
\[
 q c_0^2d_0+q^2d_0^2-8qd_0
   +(q^2+q^{-2})c_0^2-8c_0^2-h^4=c_0^2-32.              \tag{12g}
\]
For example, the off-diagonal contributions from
\(q\mathsf X\mathsf Y\mathsf Z+q^2\mathsf Z^2\) combine to
\((-q^{-1}c_0+q^{-2})s_1^4=-h^4\); the remaining terms
in (12g) are diagonal. Substitution of \(c_0=q+q^{-1}\)
and \(d_0\) proves the last equality. This completes the
all-level proof of (12d).

## 2. Fixed-turn bandwidth and operator presentation

For \(n\in\mathbb Z\), use the original repeated-turn operators
\[
 V_n=\kappa^nTR^{-n}T,\qquad
 V_nV_\ell=V_{n+\ell},\qquad D_n=V_nCV_{-n}.
 \tag{13}
\]
Crossing multiplication commutes with \(C\), so \(V_nJ=JV_n\).
For \(N\ge3\), conjugating (4) therefore gives exactly
\[
 D_{n+\sigma}
    =\frac8{c_0}I+
      \frac{q^{-\sigma}JD_n-q^\sigma D_nJ}
           {q^{2\sigma}-q^{-2\sigma}},
 \qquad \sigma=\pm1.
 \tag{14}
\]
Starting at \(D_0=C\), it follows that the Newton shifts in
\(D_n\) are contained in
\[
                         -|n|\le r-j\le1.
 \tag{15}
\]
Indeed \(J\) has shifts \(-1,0\), so each commutator step
adds at most one lower shift and no new upper shift.
This is a fixed number of bands when \(n\) is fixed.
For \(N=2\), direct multiplication gives the separate formula
\[
 V_n=\begin{pmatrix}1&in\\0&1\end{pmatrix},\qquad
 D_n=\begin{pmatrix}-4in&-4n^2\\-4&4in\end{pmatrix}.
 \tag{16}
\]

There is a quantitative bound for this conjugated multiplication,
although no corresponding bound is asserted for \(V_n\).
Equip ordinary canonical polynomials with their real norm on
\([-2,2]\), and operators with the induced norm.
The repeated-turn source proves \(\|J\|\le34N^3\).
Also \(\|C\|\le6\): if \(p\) has degree at most \(D\),
its leading coefficient has modulus at most \(\|p\|_{\mathbb R}\)
by its Chebyshev expansion, and
\(\operatorname{can}(Zp)=Zp-[Z^D]p\,P_N\).
Use \(\|P_N\|_{\mathbb R}\le4\).
For \(N\ge3\), \(c_0\ge1\) and
\(|q^2-q^{-2}|^{-1}\le N/4\).
Equation (14) thus proves, for every fixed integer \(n\),
\[
                         \|D_n\|\le C_nN^{4|n|}.
 \tag{17}
\]
The finitely sized case (16) is absorbed in \(C_n\).
This estimate does not bound the condition number of \(V_n\).

There is also a divisor-free second-order recurrence:
\[
 \boxed{\begin{split}
 qD_{n+2}+q^{-1}D_n+D_{n+1}J&=8I,\\
 q^{-1}D_{n+2}+qD_n+JD_{n+1}&=8I ,
 \end{split}\qquad n\in\mathbb Z.}                         \tag{17a}
\]
For \(N\ge3\), insert the second cyclic relation (12a) into
(14) at \(n=1,\sigma=1\). It gives
\[
 D_2=8q^{-1}I-q^{-2}C-q^{-1}D_1J.
 \tag{17b}
\]
The other ordering follows from the same cyclic relation.
Conjugate both identities by \(V_n\), using \(V_nJ=JV_n\),
to obtain (17a). At \(N=2\), substitution of (16) verifies
both identities directly, for every integer \(n\).
Thus (17a) has no exceptional denominator even at that level.

A completely finite Chebyshev formula follows. Let \(U_\ell\)
denote the ordinary Chebyshev polynomial of the second kind,
with \(U_{-1}=0,U_0=1\), only in the following display.
For \(m\ge1\),
\[
 \begin{split}
 D_m={}&q^{1-m}D_1U_{m-1}(-J/2)
       -q^{-m}C U_{m-2}(-J/2)\\
       &+8q^{-m}\sum_{\ell=0}^{m-2}
                  q^{\ell+1}U_{m-2-\ell}(-J/2).
 \end{split}                                             \tag{17c}
\]
The sum is empty at \(m=1\). Multiply the first equation in
(17a) by \(q^{n+1}\) and set \(E_n=q^nD_n\); then
\(E_{n+2}=-E_{n+1}J-E_n+8q^{n+1}I\).
The displayed finite expression solves this recurrence with
\(E_0=C,E_1=qD_1\), as direct substitution shows.
All polynomials in \(J\) are on the indicated right side;
no commutation with \(C\) or \(D_1\) was assumed.
Negative \(m\) follow by coefficient conjugation.

In particular every noncommutative polynomial operator relation
has the exact transport rule
\[
 \mathscr P(C,J)f=g
 \quad\Longrightarrow\quad
 \mathscr P(D_n,J)V_nf=V_ng.
 \tag{18}
\]
The order of the factors in \(\mathscr P\) is unchanged.
If an identity originally has scalar rational coefficients,
its scalar denominators must first be retained or cleared on
the stated parameter domain; (18) does not authorize an inverse
of a vanishing operator coefficient.

Moreover \(V_n1=1\), since \(Te_0=e_D\),
\(R^{-n}e_D=\kappa^{-n}e_D\), and \(Te_D=1\).
For any fixed number of endpoint kernels this gives
\[
 \boxed{\quad
 V_n\left(\prod_{i=1}^r K_N(w_i,C)\,1\right)
       =\left(\prod_{i=1}^r K_N(w_i,D_n)\right)1 .
 \quad}                                                   \tag{19}
\]
The products on both sides are the exact canonical products.
Their factors on the right commute because all are polynomials
in the same \(D_n\). Formula (19) is a finite quantum-operator
presentation; its degree-\(D\) kernel polynomials cannot be
estimated by (17) termwise without potentially exponential cost.

## 3. The elementary commuting principal-symbol relation

This section is a formal coefficient calculation, not an
asymptotic estimate. For an interior Newton scale \(j/N=x\),
write \(\lambda=e^{2\pi ix}\), and let \(\tau\) denote the
formal index-raising variable. Set
\[
 c=\lambda+\lambda^{-1},\qquad a=2-c.
\]
Taking the leading coefficients of (3),(5) as \(N\) increases,
with shift variables commuting at this formal leading order,
gives the Laurent symbols
\[
 \begin{split}
 X&=c-a\tau,\\
 Y&=c-a\tau^{-1},\\
 Z&=4\lambda^{-1}-2\lambda^{-2}
                         +\lambda^{-1}a(\tau+\tau^{-1}).
 \end{split}                                             \tag{19a}
\]
They satisfy the exact Laurent-polynomial identity
\[
 \boxed{\quad
 X^2+Y^2+Z^2+XYZ-8(X+Y+Z)+28=0.
 \quad}                                                   \tag{19b}
\]
Indeed, put \(S=X+Y-4\). Direct expansion of (19a) gives
\[
 XY-4=(\lambda+\lambda^{-1})S,\qquad Z-2=-S/\lambda.
 \tag{19c}
\]
Consequently \(S^2+(Z-2)^2+(XY-4)(Z-2)=0\);
expansion is (19b). The proof does not divide by \(S\),
\(a\), or any of the differences in (19b), so it retains
their degenerate values. The variables \(\lambda,\tau\)
are nonzero formal Laurent variables throughout.
No knot peripheral polynomial, integration cycle, or
source-growth conclusion is identified by this cubic.
The scalar relation itself is already recorded, in equivalent
form, in research_mixed_next_outer_paired_newton_characteristics.md
§5 (28) and in papers/nonparabolic-tree-geometry/character.tex
(C10) at boundary trace \(2\). Neither is needed for the
self-contained calculation above. The operator lift (12d)
and its exact turn and branching transport are the point here.

## 4. Exact ordinary branching and its mixed forcing

We next make explicit what the one-factor forced equation misses
at an ordinary branching vertex.
Let \(r\ge1\), let \(w_1,\ldots,w_r\) be arbitrary complex numbers,
and put
\[
 k_i(Z)=K_N(w_i,Z),\qquad
 P_r=\operatorname{can}\prod_{i=1}^r k_i,\qquad
 \lambda_r=\sum_{i=1}^r w_i-(r-1)c_0.
 \tag{20}
\]
For an index variable \(x\), write
\[
 c(x)=2\cos((2x+1)\pi/N),\quad
 a(x)=\frac{s_{x+1}^4}{s_{2x+1}s_{2x+2}},\quad
 b(x)=\frac{s_x^4}{s_{2x}s_{2x+1}},
\]
\[
 k_i^0(x)=k_i(c(x)),\quad
 \Delta_\pm k_i(x)=k_i(c(x\pm1))-k_i(c(x)).
 \tag{21}
\]
All apparent poles below are interpreted in the combined expression.
The original difference operator is
\[
 \mathcal L f(c(x))
   =c_0f(c(x))-a(x)\Delta_+f(x)-b(x)\Delta_-f(x).
 \tag{22}
\]
Its action on canonical polynomials is \(J\).
It also acts on ordinary polynomials of higher degree.
Indeed the cosine-difference calculation in the repeated-turn
source makes (22) polynomial; the same calculation applies to
every finite cosine sum. Furthermore
\[
 P_N(c(x+1))=P_N(c(x))=P_N(c(x-1))
\]
implies \(\mathcal L(P_Nh)=P_N\mathcal Lh\).
Thus this ordinary action descends to the same full quotient.

Define the mixed expression
\[
 \begin{split}
 \mathcal M_r(x)={}&
 a(x)\sum_{\substack{I\subset\{1,\ldots,r\}\\|I|\ge2}}
       \prod_{i\in I}\Delta_+k_i(x)
       \prod_{i\notin I}k_i^0(x)\\
 &+b(x)\sum_{\substack{I\subset\{1,\ldots,r\}\\|I|\ge2}}
       \prod_{i\in I}\Delta_-k_i(x)
       \prod_{i\notin I}k_i^0(x).
 \end{split}                                             \tag{23}
\]
Although its separate displayed terms use the index chart,
their sum is an ordinary polynomial in \(c(x)\). To see this
without any pole assumption, expand the finite product differences
in (22) and use the exact one-factor equations
\[
       (w_i-\mathcal L)k_i=\frac{\eta P_N(w_i)}{N^2}e_D.
 \tag{24}
\]
The result is the ordinary polynomial identity
\[
 (\lambda_r-\mathcal L)\prod_i k_i
   =\frac{\eta e_D}{N^2}
          \sum_iP_N(w_i)\prod_{\ell\ne i}k_\ell
       +\mathcal M_r.
 \tag{25}
\]
It also proves the asserted removability of the paired expression
in (23). Let \(M_r\) denote its canonical representative.

The endpoint source simplifies exactly after canonical reduction:
\[
 e_Dk_i=e_D\quad\hbox{in }\mathcal A_N.
 \tag{26}
\]
Indeed \(k_i(c_0)=1\), while \((Z-c_0)e_D=\eta P_N/N^2\).
This argument preserves the first normal, rather than merely
checking values at distinct roots.
Equations (25)--(26) give
\[
 \boxed{\quad
 (\lambda_r-J)P_r
   =\frac{\eta}{N^2}\left(\sum_iP_N(w_i)\right)e_D+M_r.
 \quad}                                                   \tag{27}
\]
For \(r=1\), \(M_1=0\), recovering the original equation.
For \(r=2\), the extra term is the canonical polynomial represented by
\(a\,\Delta_+k_1\Delta_+k_2+b\,\Delta_-k_1\Delta_-k_2\).

Since \(V_nJ=JV_n\) and
\(V_ne_D=\kappa^nT(R^{-n})\), the exact turned branching source is
\[
 \boxed{\quad
 (\lambda_r-J)V_nP_r
   =\frac{\eta\kappa^n}{N^2}
        \left(\sum_iP_N(w_i)\right)T(R^{-n})+V_nM_r .
 \quad}                                                   \tag{28}
\]
Every shared endpoint parameter and coefficient remains inside
this identity. It can be differentiated in those ordinary
parameters or multiplied by the remaining original spectator
before its trace is taken. No quotient is imposed on a free
outside variable.

For fixed \(r\), \(w_i=2\cosh(\alpha_i/N)\), and bounded complex
\(\alpha_i\), one has \(\lambda_r-2=O(N^{-2})\).
Thus the homogeneous part remains at the same microscopic
spectral scale as the one-factor equation.
However (28) retains \(V_nM_r\), not \(M_r\) before turning.
A bound for the latter does not bound the former.
The present note supplies neither a finite growing-channel
estimate nor a comparison of this mixed source with the filled
geometric action. In particular it does not iterate the
one-factor polynomial bound or discard the terminal action
already present in \(T(R^{-n})\).

## 5. An unconditional norm estimate retaining the combined forcing

There is a quantitative way to state the remaining task without
separating terms that may cancel. Fix \(\Lambda<\infty\).
For every canonical polynomial \(F\) and every
\(|\lambda-c_0|\le\Lambda/N^2\), put \(g=(\lambda-J)F\).
There are constants \(C_\Lambda,p_\Lambda\) such that
\[
 \begin{split}
 &\|g\|_{\mathbb R}+|F(c_0)|+|F'(c_0)|
                        \le C_\Lambda N^3\|F\|_{\mathbb R},\\
 &\|F\|_{\mathbb R}
       \le C_\Lambda N^{p_\Lambda}
             \{\|g\|_{\mathbb R}+|F(c_0)|+|F'(c_0)|\}.
 \end{split}                                             \tag{29}
\]
Here and below the norm is on the whole ordinary interval
\([-2,2]\). The first inequality follows from the \(J\) bound
and ordinary Markov's inequality.

For completeness, the second is the original forced row argument
with arbitrary polynomial forcing. At the regular rows
\(0\le j<\lfloor(N-1)/2\rfloor\), put
\(h_j=F(c_j)\), \(q_j=b(j)/a(j)\), and
\(d_j=(c_0-\lambda)/a(j)\). Then exactly
\[
 h_{j+1}=(1+q_j+d_j)h_j-q_jh_{j-1}
                                      +g(c_j)/a(j).
 \tag{30}
\]
The direct single-turn proof gives
\(0\le q_j<1\), \(a(j)\ge16(j+1)^2/(\pi^2N^2)\).
Thus the balanced state
\((h_j,(j+1)(h_j-h_{j-1}))\) has forward step norm
at most \(1+B_\Lambda/(j+1)\).
All its forward products are polynomial in \(N\);
its forcing is bounded by a polynomial times
\(\|g\|_{\mathbb R}\).
The first row starts from the displayed anchor \(F(c_0)\).

Differentiate the ordinary index identity (30). The state of
\(y_j=c'(j)F'(c_j)\) has the same homogeneous matrices,
with additional forcing from coefficient derivatives and from
\(g'(c_j)c'(j)\). The coefficient derivatives have polynomial
bounds, and Markov bounds \(g'\) by \(CN^2\|g\|_{\mathbb R}\).
Its initial data are controlled by \(F(c_0),F'(c_0)\);
the removable coefficient has \(b(0)=b'(0)=0\).
The same forward estimate reaches every double-root normal
without using a singular next row. Division by
\(|c'(j)|\ge8\pi/N^2\) costs only a polynomial.
The odd simple value is already in the value propagation.
At \(N=2\) the two initial anchors are the complete data.
Finally the exact value/first-normal Fourier reconstruction in
the single-turn source has polynomial conditioning on both
parities. This proves (29) for every canonical \(F\), with
no zero-free assumption and no inverse fundamental matrix.

Here are the actual anchors for the branching source. Write
\[
 Q_N(Z)=\left.\partial_wK_N(w,Z)\right|_{w=c_0},
 \qquad G_n=T(R^{-n}).
\]
Frobenius self-adjointness of \(T\) and the original kernel give
\[
 \begin{split}
 \mathcal A_0(n,P)&:=(V_nP)(c_0)
                     =\kappa^n\phi_N(G_nP),\\
 \mathcal A_1(n,P)&:=(V_nP)'(c_0)
                     =\kappa^n\phi_N\!\left[
                                 T(R^{-n}Q_N)P\right].
 \end{split}                                             \tag{31}
\]
Indeed \((Tf)(c_0)=\phi_N(f)\) and
\((Tf)'(c_0)=\phi_N(Q_Nf)\); transfer the remaining \(T\)
across the original pairing. Formula (31) keeps every product
and normal before closing.

For bounded microscopic parameters in (20), apply (29) with
\(F=V_nP_r\), \(\lambda=\lambda_r\), and the *combined* source
\[
 \mathcal G_{n,r}
     =\frac{\eta\kappa^n}{N^2}
          \left(\sum_iP_N(w_i)\right)G_n+V_nM_r.
 \tag{32}
\]
It follows unconditionally that
\[
 \boxed{\quad
 \|V_nP_r\|_{\mathbb R}
 \ \asymp_{\rm poly(N)}\
 \|\mathcal G_{n,r}\|_{\mathbb R}
       +|\mathcal A_0(n,P_r)|+|\mathcal A_1(n,P_r)|.
 \quad}                                                   \tag{33}
\]
The notation means the two explicit polynomial inequalities
of (29), with constants depending on the fixed microscopic
parameter bound and the fixed number of factors.
No triangle inequality separates the two terms in (32).
For arbitrary \(n\), the normal anchor in (31) is
\(T(R^{-n}Q_N)\); it is not \(V_nQ_N\).
In particular its bound is not inferred by differentiating
the repeated-turn kernel at the physical endpoint.
Equation (33) locates the required source estimate in the
actual combined forcing and its actual two anchors. It does
not supply a filled-action bound for those quantities.

The extra normal channel has a precise source interpretation.
Differentiating (24) at the double endpoint \(w=c_0\) gives
\[
                       (J-c_0)Q_N=1,                     \tag{34}
\]
because \(K_N(c_0,Z)=1\) and \(P_N'(c_0)=0\).
Write \(H_n=T(R^{-n}Q_N)\). From (13),
\[
 D_n=TR^{-n}JR^nT.
\]
Therefore
\[
                 (D_n-c_0)G_n=0,\qquad
                 (D_n-c_0)H_n=G_n.                       \tag{35}
\]
The first uses \((J-c_0)1=0\), and the second is (34)
with all original factors retained. In particular
\[
 \|H_n\|_{\mathbb R}
       \ge\frac{\|G_n\|_{\mathbb R}}{\|D_n\|+|c_0|}.
 \tag{36}
\]
This is a polynomial-loss lower comparison for fixed \(n\),
by (17), not an upper comparison. The original normal
anchor involves this actual Jordan companion; it cannot
be discarded as a zero endpoint term.

## 6. Direct-source readbacks

All three complete direct sources were read at their unchanged pins,
with the directly used implications and hashes checked:

* [Exact full unit-turn identities](research_full_endpoint_unit_turn_identities.md),
  SHA256 e2f69aaff28080b9dd9e11365ce18d68a9d738667917204714556681c50789e8:
  original full triangular matrix, signed crossing convention,
  endpoint reproducer, and canonical representative.
* [Repeated turns and the original difference operator](research_repeated_endpoint_unit_turn_action_growth.md),
  SHA256 92a5b15719f594668f5514cfd2decfa9a9350a784321127323153fe353084a9a:
  repeated-turn composition, original difference formula and
  kernel forcing, polynomial \(J\) norm, and retained terminal action.
* [Full single-endpoint propagation](research_full_endpoint_unit_turn_polynomial_bound.md),
  SHA256 329ee59c992c359c42775f564f540ffeee7f142bf51b5132913bf4cf2a859d35:
  regular-row coefficient bounds, differentiated forward propagation,
  and polynomial full-Hermite reconstruction at both parities.

The all-entry conjugation and mixed branching identities are proved
above. Only written mathematics, source-text reads and hashes were
used. No mathematical program, numerical experiment, test or build
was run. Adopted notes and public manuscripts are unchanged.
