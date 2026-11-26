# A polynomial boundary equation for the original four-coherent source

22 November 2026. Written research proof. Earlier final notes and public
manuscripts remain unchanged.

The original pairing of two coherent products has an exact finite
boundary equation. On a fixed product of two boundary parameters it
is a polynomial eigenfunction with a known extreme coefficient. Away
from specified color resonances, these data determine that polynomial
uniquely. At the resonances the actual polynomial family, rather than
a normalization by a vanished coefficient, retains the source.

This concerns the full Frobenius contraction. It is not a positive
orthogonality assertion, a scalar lower estimate, or a volume theorem.

## 1. The original scalar and its finite sum

Fix \(N\ge2\), and put
\[
 d=N-1,\qquad q=e^{\pi i/N},\qquad Q=q^2,\qquad
 \eta=(-1)^d,\qquad \kappa=e^{\pi i d^2/(2N)}.
 \tag{1}
\]
Use the full original algebra and the centered basis \(f_0,\ldots,f_d\)
of [C]. In particular, in its Newton basis,
\[
 \phi(e_i e_j)=\delta_{i+j,d},\qquad Je_i=e_{d-i},\qquad
 R^+=\sqrt N f_0,\quad R^-=\sqrt N f_d,\quad R^+R^-=1.
 \tag{2}
\]
All first derivatives at repeated Casimir roots are included in this
algebra and in \(\phi\). No distinct-root replacement is made.

Define unnormalized coherent polynomials and their actual scalar by
\[
 U_a=\sum_{j=0}^d a^j f_j,\qquad
 \Phi_N(y,z;s,t)=\phi(U_yU_zU_sU_t).
 \tag{3}
\]
It is a polynomial of degree at most \(d\) in each of its four
parameters. Write
\[
 \begin{split}
 D_N(a)&=1-\eta a^N,\qquad
 F_N(a)=\sum_{j=0}^d(-qa)^j=\frac{D_N(a)}{1+qa},\\
 G_N(r)&=\sum_{j=0}^d r^j,\qquad b=yz,\quad r=st.
 \end{split}
 \tag{4}
\]
The quotients in (4) denote the displayed polynomials at their
removable points. Also set
\[
 H_j(y,z)=
 \frac{(Q;Q)_j(Qyz;Q)_j}
 {(-qy;Q)_{j+1}(-qz;Q)_{j+1}},\qquad
 (a;Q)_j=\prod_{h=0}^{j-1}(1-aQ^h).
 \tag{5}
\]
The full output coefficient formula [E, equation (5)] gives
\[
 U_yU_z=\sum_{j=0}^d B_j(y,z)e_j,\qquad
 B_j(y,z)=\frac{\kappa^2(-q)^jD_N(y)D_N(z)}{N}H_j(y,z).
 \tag{6}
\]
Initially (5)--(6) can be read off the displayed denominator locus.
After cancellation they are identities of the original polynomial
family, including at its source resonances.

The elementary phase identity \(\kappa^2(-q)^d=1\), together with
(2), proves the exact finite formula
\[
 \Phi_N=
 \frac{\kappa^2D_N(y)D_N(z)D_N(s)D_N(t)}{N^2}
       \sum_{j=0}^d H_j(y,z)H_{d-j}(s,t).
 \tag{7}
\]
Thus this sum already contains the original closing and all its
Hermite channels.

For later use, reflection of the finite products gives
\[
 B_{d-j}(s,t)=G_N(r)(-q)^j
       \frac{(-q/s,-q/t;Q)_j}{(Q,Q/r;Q)_j}.
 \tag{8}
\]
Here and below a tuple in a shifted factorial means a product.
For an explicit verification, \((Q;Q)_d=N\), and
\[
 (Q;Q)_{d-j}=
   \frac{N(-1)^jQ^{j(j+1)/2}}{(Q;Q)_j}.
\]
Removing the last \(j\) factors of the other three products in
(6) produces, for \(1\le h\le j\), the ratio
\[
 \frac{(1+qsQ^{-h})(1+qtQ^{-h})}{1-rQ^{-h}}
 =-Q^{1-h}
       \frac{(1+qQ^{h-1}/s)(1+qQ^{h-1}/t)}{1-Q^h/r}.
\]
Its product and \(\kappa^2(-q)^d=1\) give exactly (8), including
the factor \((-q)^j\). No parity sign has been suppressed.

Let
\[
 \begin{split}
 \mathfrak p_N(y,z;r)&=\frac{\kappa^2}{N}F_N(y)F_N(z)G_N(r),\\
 U&=-q/s,\quad V=-q/t,\quad \mu=U+V,\quad UV=Q/r,\\
 W_j&=(U,V;Q)_j,\qquad
 a_j=\frac{Q^j(Qb;Q)_j}{(-q^3y,-q^3z,Q/r;Q)_j}.
 \end{split}
 \tag{9}
\]
Equations (6) and (8) now prove
\[
 \boxed{\quad \Phi_N=\mathfrak p_N\sum_{j=0}^d a_jW_j.\quad}
 \tag{10}
\]
The entire prefactored expression in (10), not each potentially
singular factor separately, is continued at removable parameters.
Equivalently this is the finite \(j=0,\ldots,d\) series
\[
 \Phi_N=\mathfrak p_N\,
 {}_4\phi_3\!\left(
 \begin{matrix}Q^{-d},\ Qb,\ -q/s,\ -q/t\\
                 -q^3y,\ -q^3z,\ Q/r\end{matrix};Q,Q\right).
 \tag{11}
\]
At the root, \((Q^{-d};Q)_j/(Q;Q)_j=1\) for \(j<N\).
Formula (11) means this finite series; cancellation does not authorize
extending its index beyond \(d\).

## 2. A finite triangular operator calculation

The following calculation supplies its own proof of the boundary
operator. Temporarily use a generic base \(p\), generic parameters
\(\alpha,\beta,\gamma\), and \(h=\gamma p\). For symmetric Laurent
polynomials under \(u\mapsto h/u\), define
\[
 \begin{split}
 \mathcal B(u)&=
 \frac{(u-\alpha p)(u-\beta p)(u-\gamma p)(u-h)}
 {(u^2-h)(u^2-ph)},\\
 \mathcal D(u)&=
 \frac{p(u-1)^2(\beta u-\gamma)(\alpha u-\gamma)}
 {(u^2-h/p)(u^2-h)},\\
 \mathcal L f(u)&=\mathcal B(u)[f(u/p)-f(u)]
                 +\mathcal D(u)[f(pu)-f(u)].
 \end{split}
 \tag{12}
\]
Put \(w_k(u)=(u,h/u;p)_k\), with \(w_0=1\). Then
\[
 \begin{split}
 \mathcal L w_k&=\lambda_k w_k+\chi_k w_{k-1},\\
 \lambda_k&=(p^{-k}-1)(1-\alpha\beta p^{k+1}),\\
 \chi_k&=-p^{-k}(1-p^k)(1-\alpha p^k)
                              (1-\beta p^k)(1-\gamma p^k)
                         \qquad(k\ge1).
 \end{split}
 \tag{13}
\]
Also \(\mathcal Lw_0=0\).

Here are the polynomial and endpoint details. Direct substitution
gives \(\mathcal B(h/u)=\mathcal D(u)\), so (12) preserves symmetry.
At \(u^2=ph\), the first shift exchanges \(u,h/u\), and its
difference vanishes; the other shifted fold is identical. At
\(u^2=h\), the residues of \(\mathcal B,\mathcal D\) are opposite,
and the two shifted values of a symmetric function agree. Thus these
apparent poles cancel. At zero and infinity the Laurent degree
does not increase. Every symmetric Laurent polynomial of degree at
most \(k\) is a polynomial of degree at most \(k\) in \(u+h/u\):
subtract its extreme symmetric Laurent pair and induct. Consequently
\(\mathcal Lw_k\) is such a polynomial.

At infinity, \(\mathcal B\to1\), \(\mathcal D\to p\alpha\beta\),
and the leading terms of the two shifts are \(p^{-k}\) and
\(p^k\) times the original. Their combination gives \(\lambda_k\).
At \(u=p^{-m}\), for \(0\le m\le k-2\), both neighboring
values of \(w_k\) vanish. For \(m=0\) the reverse coefficient
vanishes instead. Thus \(\mathcal Lw_k\) has all the \(k-1\)
generic roots of \(w_{k-1}\). It follows that the remaining
coefficient in (13) is a scalar \(\chi_k\).

Evaluate at \(u=p^{1-k}\). Only the forward shifted term survives.
The ratio of its first shifted factorial to the corresponding factor
of \(w_{k-1}\) is \(1-p^{-k}\). The other ratio is
\[
 \frac{(hp^k;p)_k}{(hp^{k-1};p)_{k-1}}
       =\frac{(1-hp^{2k-2})(1-hp^{2k-1})}{1-hp^{k-1}}.
\]
These factors cancel exactly against the two denominators and the
last numerator of \(\mathcal B(p^{1-k})\). What remains is
\((1-p^{-k})(1-\alpha p^k)(1-\beta p^k)(1-\gamma p^k)\),
which is the coefficient in (13). This proves the finite identity.
Clearing its rational denominators extends it to all specializations
where the resulting polynomial expressions are defined; no assertion
about distinct roots after specialization is required.

## 3. The exact original boundary equation and its folds

In (12)--(13), specialize
\[
 p=Q,\qquad \alpha=-qy,\quad\beta=-qz,\quad\gamma=r^{-1},
 \qquad u=U=-q/s.
 \tag{14}
\]
Let \(\sigma(s,t)=(Qs,Q^{-1}t)\). Direct simplification gives
\[
 \begin{split}
 B&=\frac{(t+q)^2(1-Qys)(1-Qzs)}{(t-s)(t-Qs)},\\
 D&=\frac{(s+q)^2(1-Qyt)(1-Qzt)}{(Qt-s)(t-s)},\\
 L&=B(\sigma-1)+D(\sigma^{-1}-1),\\
 \lambda_k&=(Q^{-k}-1)(1-Q^{k+2}b),\\
 \chi_k&=-Q^{-k}(1-Q^k)(1+qyQ^k)(1+qzQ^k)(1-Q^k/r).
 \end{split}
 \tag{15}
\]
Thus \(LW_k=\lambda_kW_k+\chi_kW_{k-1}\). The elementary
coefficient check for (10), directly at the root, is
\[
 a_{j+1}\chi_{j+1}
  =-Q^{-j}(1-Q^{j+1})(1-bQ^{j+1})a_j
  =(\lambda_d-\lambda_j)a_j,\qquad 0\le j<d.
 \tag{16}
\]
Here \(Q^N=1\) and \(d=N-1\) were used in the last equality.
The coefficient of \(W_d\) already has eigenvalue \(\lambda_d\).
Summing (13) therefore proves the source identity
\[
 \boxed{\quad L\Phi_N=\lambda_d\Phi_N,\qquad
                \lambda_d=(Q-1)(1-Qyz).\quad}
 \tag{17}
\]
The prefactor \(\mathfrak p_N\) is invariant under \(\sigma\),
so it has not been removed by a gauge or changed by this calculation.
Only \(0\le j\le d\) occurs in (16). There is no assumed equality
of the two endpoints of a continued summand.

For a version without a fold denominator, write \(B_{\rm num},D_{\rm num}\)
for the two numerators in (15) and set
\[
 \Delta=(t-s)(t-Qs)(Qt-s).
\]
Then the exact polynomial identity is
\[
 \boxed{\quad
 \lambda_d\Delta\Phi_N
 =B_{\rm num}(Qt-s)(\sigma\Phi_N-\Phi_N)
  +D_{\rm num}(t-Qs)(\sigma^{-1}\Phi_N-\Phi_N).
 \quad}
 \tag{18}
\]
It holds for all four complex parameters, including \(s=0,t=0\),
the shifted folds, and every individual color resonance. It was
proved on a dense open set and both sides are polynomials. At a
fold, source derivatives are retained by differentiating this whole
polynomial identity. In particular, no value-only boundary condition
is substituted for the full source there. Coincident shifted folds
at \(N=2\) require no exception to (18). The argument uses only
\(Q^j\ne1\) for \(0<j<N\), so composite levels are included.

There is a precise generic-base caution. If \(n=N-1\) is fixed
and the base is moved to \(p\), the terminating series associated
with (12) has second numerator
\[
 \alpha\beta p^{n+1}=p^{N+1}yz,
 \qquad
 \lambda_n=(p^{1-N}-1)(1-p^{N+1}yz),\qquad q^2=p.
 \tag{19}
\]
Keeping the root expression \(Qyz\) unchanged during that movement
would give the wrong auxiliary eigenfunction. This note instead uses
the root coefficient check (16). Its generic calculation (12)--(13)
is a finite rational proof device, not an identification of a
generic-\(q\) quantum source or of its quantum-normal derivatives.

## 4. The selected polynomial and its resonant family

Fix \(r\ne0\). Since \(\Phi_N(y,z;s,r/s)\) is symmetric under
\(s\leftrightarrow r/s\), it is a polynomial of degree at most \(d\)
in \(\mu=-q(s+t)/r\). The \(W_k\), \(0\le k\le d\), form a
basis: their leading coefficients in \(\mu\) are
\((-1)^kQ^{k(k-1)/2}\), which do not vanish.

Its leading coefficient is known from the original source:
\[
 \boxed{\quad [\mu^d]\Phi_N
             =\frac{\kappa^2r^d}{N}G_N(yz).\quad}
 \tag{20}
\]
Indeed the coefficient of \(s^d\) at fixed \(r\) is
\(\phi(U_yU_zf_df_0)=\phi(U_yU_z)/N=G_N(yz)/N\), by (2)
and \(\phi(f_af_b)=\delta_{ab}\). Since the extreme term of
\(\mu^d\) is \((-q/r)^ds^d\), (20) follows from
\((-q)^{-d}=\kappa^2\).

For \(0\le k<d\),
\[
 \lambda_d-\lambda_k
       =-Q^{-k}(1-Q^{k+1})(1-yzQ^{k+1}).
 \tag{21}
\]
Consequently, if \(yz\notin\{Q^{-1},\ldots,Q^{-d}\}\), the
triangular equation (17), restricted to degree at most \(d\),
has a unique eigenpolynomial with the leading coefficient (20).
That coefficient is nonzero, since precisely the excluded values
are the zeros of \(G_N(yz)\). This determines the original
four-boundary source without fitting an unknown closed period.

At \(yz=Q^{-h}\), \(1\le h\le d\), the actual source satisfies
\[
                         \deg_\mu\Phi_N\le h-1.
 \tag{22}
\]
To see this, work first where the other displayed denominators do
not vanish. The factor \((Qyz;Q)_j\) is zero for every \(j\ge h\),
so (10) has degree at most \(h-1\). The higher polynomial
coefficients then vanish identically on this color fiber by
continuation, including its simultaneous resonances. A normalization
by (20) at that fiber would discard the actual source.

The original polynomial family in \(y,z,s,t\) supplies its full
continuation. For example, fixing \(y\ne0,r\ne0\) and writing
\(z=b/y\), differentiation gives, off the fold denominators,
\[
 (L_b-\lambda_d(b))\partial_b\Phi_N
       =(\lambda_d'(b)-\partial_bL_b)\Phi_N.
 \tag{23}
\]
At the folds the same statement is read by differentiating (18).
All derivatives of the known prefactor are included. These are
external parameter derivatives; the internal repeated-root Hermite
data were already present in (2)--(7). No extension in the quantum
level is inferred from this family statement.

## 5. Two exact source readouts and actual gluing

The centered compiler gives
\(U_{ja}=\kappa(-q)^j(-qQ^j)^a/\sqrt N\). The finite geometric
sum therefore proves, with their original phases,
\[
             U_{-q}=\kappa^{-1}\sqrt N e_d,\qquad
             U_{-q^{-1}}=\kappa\sqrt N\,1.
 \tag{24}
\]
The Newton factors show that \(m\) is evaluation at the first
Casimir node: every \(e_j\), \(j>0\), vanishes there. Thus it is
an algebra character. In particular,
\(\phi(e_dv)=m(v)\) and \(m(U_a)=\kappa F_N(a)/\sqrt N\). Hence
\[
 \boxed{\quad
 \Phi_N(y,z;-q,t)=\frac{\kappa^2}{N}F_N(y)F_N(z)F_N(t),
 \qquad
 \Phi_N(y,z;-q^{-1},t)=\kappa\sqrt N\,\mathcal C_N(y,z,t).
 \quad}
 \tag{25}
\]
Here \(\mathcal C_N(y,z,t)=\phi(U_yU_zU_t)\) is the original
three-coherent generating scalar, including its entire source.
The first identity also follows from (10): at \(s=-q\), \(U=1\),
all \(W_j\) with \(j>0\) vanish, leaving its original prefactor.
Both identities hold at both parities, including \(N=2\).

Finally, \(\phi(Jv\,Jw)=\phi(vw)\) follows directly from (2).
Put \(u_N(a)=U_a/\sqrt{Z_N(a)}\), where
\(Z_N(a)=\sum_{j=0}^d|a|^{2j}\). The actual closing of two
turned coherent products is
\[
 \phi\!\left(J(u_N(y)u_N(z))J(u_N(s)u_N(t))\right)
 =\frac{\Phi_N(y,z;s,t)}
        {\sqrt{Z_N(y)Z_N(z)Z_N(s)Z_N(t)}}.
 \tag{26}
\]
The root shifts in (15) preserve these four normalization factors.
There is no replacement of this bilinear closing by a Hermitian
norm. Equations (17)--(26) describe a universal four-boundary
primitive, not a new knot case or closure theorem for arbitrary trees.

## 6. Coverage, scope, and complete proof sources

The terminating series in (11) has the standard \(q\)-Racah parameter
pattern. See Koekoek--Swarttouw, [equation (3.2.1)](https://tudelft.roelofkoekoek.nl/documents/as98.pdf),
with parameters \(\alpha=-qy,\beta=-qz,\gamma=(st)^{-1},\delta=1\).
Its standard difference equation is recorded there as (3.2.6).
These are coverage references, not proof premises: (12)--(18) give
the finite calculation here. No novelty is claimed for the named
polynomial or its general difference equation, and no positive
finite orthogonality theorem is used.

The new source statements identify the literal four-coherent period,
its known normalization, its full resonant family, and its exact unit
and socle readouts. No nonzero value at an arbitrary boundary point,
geometric action estimate, positive-cycle metric, or finite-exception
volume theorem follows. Scalar cancellation remains in the original
source polynomial.

The two complete proof directs were read at the matching pins below.
Only their exact full algebra, coefficient, and phase formulas are
used; no asymptotic theorem is imported.

| Label | Complete source | SHA256 |
|---|---|---|
| E | notes/research_centered_coherent_product_energy.md | 73152328a77ba5d63a2a8eaa17647ed38b7683c613e0947e3bda9e451dda76e2 |
| C | notes/research_centered_fourier_conway_compiler.md | 0edbabe42280d70e4d5dcbcb55b188a3e773c14b99fbd212eb0fe8c5b176a413 |

Only written mathematics, text reads and edits, a primary-source
coverage lookup, and metadata hashes were used. No mathematical
programs, tests, numerical experiments, builds, or git operations
were run. This research proof is author-final.
