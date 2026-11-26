# The minimal module of all restored cap observations

Private written proof, 17 November 2026. The original adjacent cap
observes exactly \(N\) independent attachment moments when both
protected variables are restored. Their quotient carries one
nilpotent Jordan block and an explicit finite transport with a
cocycle law. This quotients only data invisible to every such cap
observation. The final scalar still uses its prescribed single row.

## 1. Original source and independent probes

Use the complete fixed-root source of [I], [A], and [J]. Set
\[
 N\ge3,\quad d=N-1,\quad q=e^{\pi i/N},\quad
 \sigma=\pm1,\quad \tau=q^{2\sigma},\quad
 a=-q^\sigma,\quad \lambda=q^{\sigma d^2/2}.
 \tag{1}
\]
Keep the original lift of \(\lambda\). Let \(\mathcal B\) be a
commutative complex coefficient algebra containing every external
attachment parameter. The source-exact module of [I] is
\[
 E_N=\mathcal B[c,y]/(c^N,y^N),\qquad
 D_c=D_{\tau,c},\quad D_y=D_{\tau^{-1},y},\qquad
 \ell(F)=[t^d]F(at,t).
 \tag{2}
\]
Both derivatives descend, commute, and have \(N\)-th power zero.
This quotient is exact for the specified coefficient target, not
for pointwise values on an ordinary complex face chart.

Introduce probe variables \(\xi,\zeta\) independent of \(\mathcal B\).
For an arbitrary attachment \(F\), the exact restored cap is
\[
 \mathcal C_F(\xi,\zeta)
 =[c^dy^d]H_\sigma(\xi,\zeta,c,y)F
 =\lambda\ell\bigl(\mathscr T(\xi,\zeta)[F]\bigr),
 \qquad
 \mathscr T=e_\tau(-\tau^{-1}\xi D_y)
                 e_{\tau^{-1}}(-\tau\zeta D_c),
 \tag{3}
\]
where \(e_\theta(U)=\sum_{k=0}^dU^k/[k]_\theta!\).
All factorials displayed have index less than \(N\).
The rectangular product in (3) has the same original row as the
triangular cap adjoint in [A]; their additional terms disappear
only after that row, as proved in [I].

The attachment may itself depend on actual protected variables
\(X,Z\), included in \(\mathcal B\). Apply (3) with independent probes
first, and then substitute \(\xi=X,\zeta=Z\). This retains every
attachment derivative and repeated incidence. The common-kernel
statement below concerns independent probes; specializing them
first can create further cancellations between parameter-dependent
moments.

## 2. The exact common kernel and its rank

The key identity of rows is
\[
 \ell D_y=-\tau a\,\ell D_c.
 \tag{4}
\]
For a basis monomial \(c^iy^j\), either both sides are zero or
\(i+j=d+1=N\). In the latter case
\([j]_{\tau^{-1}}=-\tau[i]_\tau\), and the two powers of \(a\)
are \(a^i\) and \(a^{i-1}\). This proves (4), including the
zero endpoint factors. Commutativity then gives
\[
 \ell D_y^kD_c^l=(-\tau a)^k\ell D_c^{k+l};
 \qquad \ell D_y^kD_c^l=0\quad(k+l\ge N).
 \tag{5}
\]

Define
\[
 m_r(F)=\ell D_c^rF\quad(0\le r\le d),\qquad
 K_N=\bigcap_{r=0}^d\ker m_r,\qquad Q_N=E_N/K_N.
 \tag{6}
\]
These rows are independent over \(\mathcal B\), with a split
surjective moment map. Indeed
\[
 m_s(c^dy^r)
 =\mathbf1_{s=r}\,
   \frac{[d]_\tau!}{[d-r]_\tau!}a^{d-r},
 \tag{7}
\]
and every displayed diagonal coefficient is a nonzero complex
constant. Thus \(Q_N\) is free of rank \(N\), while \(K_N\) is free
of rank \(N^2-N\).

The kernel in (6) is precisely the set of attachments invisible
to all restored cap observations:
\[
 \mathcal C_F(\xi,\zeta)=0\text{ in }\mathcal B[\xi,\zeta]
       \quad\Longleftrightarrow\quad F\in K_N.
 \tag{8}
\]
One implication follows from (3)--(5). For the other set
\(\zeta=0\): the coefficient of \(\xi^r\) is
\(\lambda a^rm_r(F)/[r]_\tau!\), a unit multiple of \(m_r(F)\).
Consequently any linear quotient through which every probe
observation factors can discard only a submodule of \(K_N\).
The quotient \(Q_N\) is the minimal one retaining all these
observations, rather than merely the value at \(\xi=\zeta=0\).

## 3. One polynomial normal coordinate

There is an explicit realization on polynomials of degree at most \(d\):
\[
 \pi F(w)=\sum_{r=0}^d\frac{m_r(F)}{[r]_\tau!}w^r,
 \qquad Q_N\simeq\mathcal B[w]_{\le d}.
 \tag{9}
\]
On the original monomial basis this is
\[
 \pi(c^iy^j)=
 \begin{cases}
 {i\brack d-j}_\tau a^{d-j}w^{i+j-d},&i+j\ge d,\\
 0,&i+j<d,
 \end{cases}
 \qquad 0\le i,j<N.
 \tag{10}
\]
Formula (7) proves surjectivity and identifies its kernel with
\(K_N\). There is the particularly simple exact section
\(\iota(g)=y^dg(c)\): (10) gives \(\pi\iota=I\).
Consequently
\(E_N=K_N\oplus y^d\mathcal B[c]_{\le d}\) as linear modules.
The derivative actions and the original row become
\[
 \pi D_c=D_{\tau,w}\pi,\qquad
 \pi D_y=-\tau aD_{\tau,w}\pi,\qquad
 \ell=\operatorname{ev}_{w=0}\pi.
 \tag{11}
\]
For example \(m_r(D_cF)=m_{r+1}(F)\), with \(m_N=0\);
(4) gives the second identity. Thus \(K_N\) is stable under both
derivatives and under \(\mathscr T\) and its inverse.
Write \(D=D_{\tau,w}\) on (9). Since
\(D^dw^d=[d]_\tau!\ne0\) and \(D^N=0\), it has exactly one
Jordan block of length \(N\).

These are linear derivative-module statements. They do not
identify a fused Hopf module or a multiplicative quotient of the
attachment algebra. In fact \(1\in K_N\), but
\(\ell(c^d)=a^d\ne0\), so \(K_N\) is not an ideal for ordinary
attachment multiplication. A neighboring operation must preserve
this actual kernel before it can descend.

## 4. Exact generating function and flat finite transport

On \(Q_N\), the original rectangular transform is
\[
 \overline{\mathscr T}(\xi,\zeta)
   =e_\tau(a\xi D)e_{\tau^{-1}}(-\tau\zeta D)
   =e_\tau(a\xi D)e_\tau(\tau\zeta D)^{-1}.
 \tag{12}
\]
Here \([l]_{\tau^{-1}}!=\tau^{-l(l-1)/2}[l]_\tau!\);
the finite dual-exponential identity of [I] proves the inverse.
Grouping degree \(r=k+l<N\) by the Gaussian binomial formula gives
\[
 \overline{\mathscr T}(\xi,\zeta)
 =\sum_{r=0}^d
    \frac{\prod_{j=0}^{r-1}(a\xi-\tau^{j+1}\zeta)}
         {[r]_\tau!}D^r.
 \tag{13}
\]
Therefore the full original cap generating polynomial is
\[
 \boxed{\quad
 \mathcal C_F(\xi,\zeta)
 =\lambda\sum_{r=0}^d
     \frac{a^rm_r(F)}{[r]_\tau!}
       \prod_{j=0}^{r-1}(\xi+q^\sigma\tau^j\zeta).
 \quad} \tag{14}
\]
Empty products equal one. This includes all boundary orders and
the actual endpoint \(r=d\), with no division by \([N]_\tau\).
It also shows that the one-probe slice
\(\mathcal C_F(\xi,0)=\lambda\pi F(a\xi)\) already determines
every restored observation.

For independent scalar parameters \(s,t\), set
\[
 U(s,t)=e_\tau(sD)e_\tau(tD)^{-1}.
 \tag{15}
\]
Then, exactly at every level,
\[
 U(s,t)U(t,u)=U(s,u),\qquad U(s,t)^{-1}=U(t,s),
 \qquad U(s,s)=I.
 \tag{16}
\]
There is also a finite logarithm:
\[
 \log U(s,t)=
 \sum_{r=1}^d\frac{(1-\tau)^r}{r(1-\tau^r)}
                  (s^r-t^r)D^r.
 \tag{17}
\]
To verify it without an infinite root specialization, work modulo
\(v^N\). The finite series satisfies
\(e_\tau(\tau v)=(1-(1-\tau)v)e_\tau(v)\).
Taking the finite nilpotent logarithm and comparing the coefficient
of \(v^r\), for \(1\le r<N\), proves (17). All its denominators
are units. Equations (15)--(17) give an explicit fundamental frame
for this local normal transport; they introduce no new source
normalization.

The actual endpoints of (15) are \(s=a\xi,t=\tau\zeta\).
On the exact line
\[
 \zeta=-q^{-\sigma}\xi,\qquad
 \overline{\mathscr T}(\xi,\zeta)=I,\qquad
 \mathcal C_F(\xi,\zeta)=\lambda\ell(F).
 \tag{18}
\]
For a parameter-dependent attachment, \(F\) on the right is still
evaluated at those parameter values. Its parameter dependence has
not been deleted. Formula (18) is an operator identity on \(Q_N\),
not an identity of the rectangular operator on all of \(E_N\).

## 5. Bounds and the unchanged scalar obligation

On a complex parameter fiber give \(E_N\) the weighted coefficient
norm of [I], with positive radii \(r_c,r_y\), and give \(Q_N\) its
quotient norm. Stability of \(K_N\) in both directions lets the
exact bounds in [I] descend:
\[
 \|\overline{\mathscr T}^{\,\pm1}\|\le B_N,\qquad
 \|\overline{\mathscr T}^{\,\pm1}-I\|\le B_N-1,\qquad
 B_N=(1+|\xi|/r_y)^d(1+|\zeta|/r_c)^d.
 \tag{19}
\]
Thus transport is bounded in both directions on the \(N^{-1}\)
protected scale and is \(I+O(N^{-1})\) on the \(N^{-2}\) scale.
Buffered holomorphic parameter estimates have the same fixed
derivative interpretation as [I]. No uniform comparison with an
unweighted moment-coordinate norm is asserted.

The original source has become the exact row
\(\lambda\operatorname{ev}_0\) after the transport (12).
This row still has a kernel. For instance the nonzero moment
class represented by \(c^dy\) has \(m_0=0\) and \(m_1\ne0\).
An invertible \(U(s,t)\), or preservation of all restored data,
does not force its prescribed scalar observation to be nonzero.
For a full homogeneous original attachment the final remaining
coefficient targets retain the cancellations stated in [A];
they are not replaced by all independent probe coefficients.

There is a concrete terminal statement for the full original
homogeneous source in [A]. Suppose the selected crossing has the
four distinct face variables \(X,Z,c,y\), and the numerator has
\(R\) boxes of degree \(d\) and \(R\) ordinary targets of degree
\(d\). Extract all \(R-2\) ordinary targets other than \(c,y\)
from the product of the other \(R-1\) boxes. The resulting
attachment \(F_{\rm term}(X,Z,c,y)\), if nonzero, is homogeneous
of total degree \(d\). Therefore
\[
 \pi F_{\rm term}(w)=\gamma_N\,1,\qquad
 \overline{\mathscr T}\,\pi F_{\rm term}=\gamma_N\,1,\qquad
 [c^dy^d]H_\sigma F_{\rm term}=\lambda\gamma_N .
 \tag{20}
\]
Indeed (10) kills every term of \(c,y\)-degree below \(d\).
Among terms of total degree \(d\), the surviving ones consequently
have \(X,Z\)-degree zero and yield \(w\)-degree zero. Thus
\(\gamma_N\) is independent of \(X,Z,w\), while retaining every
other source parameter and normalization. The constant polynomial
line in (9) is \(D\)-horizontal; its coefficient \(\gamma_N\)
is not asserted to be a unit or even nonzero. Equation (20)
explains the exact terminal invariance without computing that
coefficient or its size.

The result is a source-exact reduction for the selected adjacent
crossing and its entire attachment. Coefficient extractions in
external variables commute with (14). Arbitrary multiplication
or different turns reusing the discarded \(c,y\) data are not
assigned an action on \(Q_N\) without proving preservation of \(K_N\).
No geometric critical-field action, off-root identity, pointwise
face replacement, or lower bound for a fixed short component is
inferred.

## Complete direct sources and coverage

All three complete texts and their used implications were read.
The earlier twist-observation tomography concerns different
Hermite crossing observations; the nilpotent Mobius source note
concerns a different framing action. Neither supplies the joint
restored-cap kernel (6). This proof uses only written algebra.

| Label | Source | SHA-256 |
|---|---|---|
| I | [Invertible cap normal translation](research_invertible_cap_normal_translation.md) | 8f53a0d2a0c2a0009310392c88bfd0c4cdd82a089a82fbf567f6b7a4a7cff2d2 |
| A | [All-jet cap attachment transform](research_protected_cap_all_jet_attachment_transform.md) | e45d2bef26c57011537a144c7e156eedf60f0bc05e3d7714edb45413ca9284b9 |
| J | [Original crossing Jackson boundary jets](research_crossing_jackson_boundary_jets.md) | 231d70047a49834c3df1f3cd722a704ec841c704a5213e5cf1d45caabc236bb7 |
