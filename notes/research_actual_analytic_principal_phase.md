# Convergence of the principal phase of the actual cut source

Private written proof, 18 November 2026.

The one-variable reduction in [B] gives a formal phase
\(\Phi(z,x)\) and a formal linear clock term \(\Theta(z,x)\).
Here both series are proved convergent near the simple node.
The proof constructs the phase through finite analytic implicit
equations for the literal crossings, their composition, and the
regular trace contractions.

This is a local result about the principal phase. It proves neither
convergence of the quantum amplitude nor occurrence of the resulting
stationary contribution in the physical invariant. In particular it
does not settle any additional filling case.

## 1. The precise assertion

Use the original one-component highest-cut source of [F], with
\(Q=e^h\), \(x=x_0e^{-h/2}\), \(Y=x_0^2\).
Assume the simple two-branch node hypotheses of [C, Section 1].
Thus \(z=Y-\alpha\), \(\alpha\ne0,1\), and the calibrated coefficient
\(\sigma\) of [C] is nonzero. The highest-cut projector remains
\(T_0=\operatorname{diag}(0,1,\ldots,1)\).

Keep independent stage marks \(e^{t_i}\), at the same stages as the
original clocks. The original mark specialization is \(t_i=hm_i\);
a fixed linear specialization of the stage marks gives any chosen
matching-lattice clocks. All vector statements below pass through
that same specialization.

The formal reduction of [B] has
\[
 -zt+\sum_{j\ge1}h^jU_j(z,m;t)
  =h^{-1}\Phi(z,x)+A_0(z,x)+m\cdot\Theta(z,x)+O(h),
 \qquad x=ht.
 \tag{1}
\]
The scalar \(t\) in (1) is the soft moment variable, distinct from
the independent stage-mark vector \(\mathbf t=(t_i)\).

**Theorem.** There is a holomorphic germ
\(\Psi(z,x,\mathbf t)\), at \((0,0,0)\), such that
\[
 \Phi(z,x)=-zx+\Psi(z,x,0),\qquad
 \Theta_i(z,x)=\partial_{t_i}\Psi(z,x,0)
 \tag{2}
\]
as coefficientwise identities with the formal series of [B].
Consequently both series in (2) converge. The holomorphic phase
\[
 \Phi_{\mathbf t}(z,x)=-zx+\Psi(z,x,\mathbf t)
 \tag{3}
\]
has a unique small holomorphic critical point \(x_g(z,\mathbf t)\).
At zero marks,
\[
 \begin{split}
 x_g(z,0)&=\frac{z}{2\sigma}+O(z^2),\\
 S_g(z)&:=\Phi_0(z,x_g(z,0))
                  =-\frac{z^2}{4\sigma}+O(z^3),\\
 \Theta_g(z)&:=\Theta(z,x_g(z,0))
                  =\frac{\mu z}{2\sigma}+O(z^2).
 \end{split}
 \tag{4}
\]
In particular the formal leading marked/unmarked ratio in [B]
is the Taylor series of the nonzero holomorphic function
\(\exp(m\cdot\Theta_g(z))\), for every fixed \(m\).

The proof does not assert convergence of \(A_0\), the remaining
quantum expansion, an operator logarithm, or a Laplace integral.
The term “principal phase” below always means the coefficient of
\(h^{-1}\) after scaling the creation and differentiation variables
by \(h^{-1/2}\). It does not mean the logarithm of a trace.

## 2. A formal Poisson calculation with a convergent answer

Let \(V(s_1,\ldots,s_d)\) be holomorphic near zero and \(V=O(s^2)\).
Define the Poisson functional algebraically by
\(\mathbb E_\lambda (N)_a=\lambda^a\), independently in each
coordinate. Consider
\[
 Z_h(U)=\mathbb E_{U/h}\exp\bigl(V(hN)/h\bigr).
 \tag{5}
\]
This expression is formal. First expand in positive \(h\)-orders
before applying the functional, and then complete in \(U\).
For each \(U\)-degree and resulting \(h\)-order the operations
below involve finitely many coefficients.

The connected factorial-moment argument of [H, Section 2] says
that a cumulant of \(v\) polynomial vertices of degrees \(d_i\)
has Poisson-parameter degree at most \(\sum d_i-v+1\).
A vertex from a homogeneous degree-\(d_i\) term of \(V(hN)/h\)
has \(h\)-order \(d_i-1\). After \(U/h\) substitution a connected
term therefore has \(h\)-power at least \(-1\). Hence
\[
                   \log Z_h(U)=h^{-1}F(U)+O(h^0).
 \tag{6}
\]
Here \(F=O(U^2)\). At fixed \(U\)-degree \(d\), its principal
coefficient comes from total original \(h\)-order \(d-1\), so
it is finite.

We now determine \(F\). The exact Poisson reweighting formula is
\[
 \frac{\mathbb E_{U/h}
       \bigl[e^{h a\cdot N}e^{V(hN)/h}\bigr]}{Z_h(U)}
 =\exp\!\left(\sum_i\frac{U_i(e^{ha_i}-1)}h\right)
                \frac{Z_h(Ue^{ha})}{Z_h(U)} .
 \tag{7}
\]
It follows first for polynomials from the falling-factorial
identity and then coefficientwise for the displayed series.
Using (6), the constant \(h\)-coefficient of (7) is
\[
                 e^{a\cdot u},\qquad
             u_i=U_i(1+\partial_iF).
 \tag{8}
\]
Thus the leading reweighted moments of every polynomial in \(hN\)
are its values at \(u\). This statement extends coefficientwise
to the analytic power series needed here.

The Poisson difference identity also gives exactly
\[
 h\,\partial_{U_i} Z_h
   =\mathbb E_{U/h}
       \left[e^{V(h(N+e_i))/h}-e^{V(hN)/h}\right].
 \tag{9}
\]
The exponent difference has leading term \(\partial_i V(hN)\).
Divide (9) by \(Z_h\), take its constant \(h\)-coefficient, and
use (8). The result is
\[
 1+\partial_iF=e^{\partial_iV(u)},\qquad
                   u_i=U_i e^{\partial_iV(u)}.
 \tag{10}
\]
No \(U_i\) has been divided out.

The second system in (10) has identity Jacobian in \(u\) at
\(U=u=0\). The analytic implicit function theorem gives a unique
holomorphic \(u(U)\). Set
\[
 F_{\rm an}(U)=V(u)+
                   \sum_i\bigl(u_i-U_i-u_i\partial_iV(u)\bigr).
 \tag{11}
\]
This is holomorphic even when some or all \(U_i\) vanish.
Differentiating (10) gives
\(du_i=e^{\partial_iV(u)}dU_i+u_i\,d(\partial_iV(u))\).
Substitution into \(dF_{\rm an}\) yields
\[
        dF_{\rm an}
          =\sum_i(e^{\partial_iV(u)}-1)dU_i.
 \tag{12}
\]
Thus (11) satisfies (10), has value zero at zero, and has precisely
the formal series \(F\) from (6). This proves convergence of that
principal series.

We will also need its stability under lower-degree corrections.
For a general vertex \(h^jv_{j,d}(N)\), \(d\le j+1\), call
\(j+1-d\) its defect. A connected collection of such vertices,
after the Poisson substitution, has \(h\)-power at least
\[
                    \sum (j+1-d)-1 .
 \tag{13}
\]
Therefore its principal coefficient uses only defect-zero
vertices. Offsets and all other lower-index-degree terms in the
literal entries do not affect this coefficient.

## 3. The analytic potentials of the two literal crossings

All logarithms in this section are the holomorphic germs with value
zero at \(s=0\). For \(Y\) in a small disk about \(\alpha\), put
\[
 \begin{split}
 f(s)&=\log\frac{e^s-1}{s},
       &F(s)&=\int_0^s f(v)\,dv,\\
 g_+(s)&=\log\frac{1-Y^{-1}e^s}{1-Y^{-1}},
       &G_+(s)&=\int_0^s g_+(v)\,dv,\\
 g_-(s)&=\log\frac{1-Ye^s}{1-Y},
       &G_-(s)&=\int_0^s g_-(v)\,dv .
 \end{split}
 \tag{14}
\]
They are holomorphic jointly in \(Y,s\); \(F,G_\pm=O(s^2)\).

Use scaled index variables \(N,C,B\) for the positive crossing,
whose unscaled indices are \(n,c=a-n,b\). Its entry-logarithm
has top-degree potential
\[
 V_+(N,C,B)
    =CB+F(N+C)-F(N)-F(C)
                         +G_+(N+C)-G_+(C).
 \tag{15}
\]
For the negative crossing use unscaled \(n,c=b-n,a\), denoting
their scaled versions by \(N,C,A\). Its potential is
\[
 V_-(N,C,A)
    =-A(N+C)+F(N+C)-F(N)-F(C)
                         +G_-(-C)-G_-(-N-C).
 \tag{16}
\]

Here is a direct coefficient check. The factorial unit in
\((Q;Q)_L\), after removing \((-h)^L L!\), has logarithm
\(\sum_{r=1}^L f(hr)\). If \(f(s)=\sum_{j\ge1}f_js^j\),
the highest degree of its order-\(h^j\) coefficient is
\(f_j L^{j+1}/(j+1)\). Polynomial summation, or the elementary
falling-factorial sum in [F], proves this assertion. Its top
series is \(F(hL)/h\). The Gaussian binomial gives the three
terms in \(F\) in (15) and (16).

For the positive color product the exponents, at fixed \(Y\),
are \(c+1,\ldots,c+n\). Summing their top powers gives the
integral from \(C\) to \(C+N\), and hence the \(G_+\) difference.
For the negative product the exponents are
\(-n-c,\ldots,-c-1\), giving the integral from \(-N-C\) to
\(-C\). Its monomial in \(Q\) contributes \(-A(N+C)\);
the positive monomial contributes \(CB\). These are precisely
the entries of [F, (2)] with \(x=x_0e^{-h/2}\).
The \(x\)-power drift and the integer endpoint offsets have
lower index degree and are excluded from the principal
coefficient by (13), rather than deleted from the source.

For clarity, the Poisson means of the positive kernel are
\[
 U=(1-Y^{-1})Z_1P_1,\quad
 V=Y^{-1/2}Z_2P_1,\quad W=Y^{-1/2}Z_1P_2;
 \tag{17}
\]
for the negative kernel they are
\[
 U=(1-Y)Z_2P_2,\quad
 V=Y^{1/2}Z_1P_2,\quad W=Y^{1/2}Z_2P_1.
 \tag{18}
\]
These are [H]'s exact kernel means. On replacing \(Z,P\) by
\(h^{-1/2}Z,h^{-1/2}P\), they become \(U/h,V/h,W/h\).
Equations (10)--(12), with (15) or (16), consequently construct
the principal logarithm of the kernel divided by its classical
kernel. Every remaining logarithmic vertex has positive defect
by (13). Substituting \(P\mapsto L_\pm^{-1}P\) then gives the
principal phase of the relative operator
\(R_\pm\Gamma(L_\pm)^{-1}\), exactly as in [H].

It is holomorphic in the fields and \(Y\). Since its Poisson
series starts in degree two in the bilinear means, its field
Taylor series begins in degree four. It is balanced: creation
and differentiation degrees are equal.

## 4. Gaussian contractions and finite composition

We give the analytic calculation needed both for composition
and for the regular trace contractions. Let \(K\) be a symmetric
complex matrix, possibly singular, and let
\[
 \mathbb E_{hK}e^{a\cdot X}=e^{h a^TKa/2}.
 \tag{19}
\]
This is an algebraic Wick functional. Suppose \(P\) is analytic,
has no constant or linear field terms for any auxiliary parameters,
and is \(O(q^3)\) at zero auxiliary parameters. Terms quadratic
in \(q\), vanishing with those parameters, are permitted.
They are first treated in the parameter-adic topology.
Define formally
\[
 Z_h(q)=\mathbb E_{hK}\exp\bigl(P(q+X)/h\bigr).
 \tag{20}
\]

In its connected logarithm a graph with \(v\) vertices and \(e\)
Wick edges contributes \(h^{e-v}\). Connectedness gives
\(e\ge v-1\), including when self-contractions are allowed.
The coefficient of \(h^{-1}\) uses exactly the connected trees.
At each fixed external degree only finitely many such trees
occur: if all vertices have degree at least three, then
\(3v\le2(v-1)+d\), so \(v\le d-2\).
Quadratic vertices each cost one auxiliary-parameter degree,
which gives the same finiteness with those degrees also fixed.
Vertices coming from nonprincipal terms of the exponent add
positive \(h\)-powers and cannot change this coefficient.
Write
\[
                    \log Z_h=h^{-1}P_{\rm eff}+O(h^0).
 \tag{21}
\]

The exact Gaussian source-translation identity gives
\[
 \frac{\mathbb E_{hK}
     [e^{a\cdot(q+X)}e^{P(q+X)/h}]}{Z_h(q)}
 =e^{a\cdot q+h a^TKa/2}\frac{Z_h(q+hKa)}{Z_h(q)} .
 \tag{22}
\]
It follows by applying (19) to exponential generators.
Thus the constant \(h\)-coefficient on the left is \(e^{a\cdot u}\),
where \(u=q+K\nabla P_{\rm eff}\). Differentiating (20) in \(q\)
and using this factorization proves
\[
 \nabla P_{\rm eff}=\nabla P(u),\qquad
                          u=q+K\nabla P(u).
 \tag{23}
\]
The Jacobian in \(u\) is the identity at zero fields and zero
auxiliary parameters. The analytic implicit function theorem
therefore solves (23), without an inverse of \(K\). Moreover
\[
 P_{\rm eff}(q)
      =P(u)-\tfrac12\nabla P(u)^T K\nabla P(u).
 \tag{24}
\]
Differentiating the right side using (23) gives
\(\nabla P(u)\cdot dq\). Its constant equals the formal value:
at \(q=0\), the small solution is \(u=0\) and both sides vanish.
Equations (23)--(24) identify the formal tree series with a
holomorphic function. The same proof is uniform in additional
holomorphic parameters on smaller disks.

The normal-symbol product after field scaling is
\[
 A\star_h B
  =\left.e^{h\partial_r\cdot\partial_s}
       A(Z,P+r)B(Z+s,P)\right|_{r=s=0}.
 \tag{25}
\]
This is (20) with the symmetric block matrix having off-diagonal
identity blocks. For principal phases \(P_A,P_B\), its effective
phase can equivalently be written
\[
 P_A(Z,P+r)+P_B(Z+s,P)-r\cdot s,
 \quad
 r=\partial_ZP_B(Z+s,P),\quad
 s=\partial_PP_A(Z,P+r).
 \tag{26}
\]
These equations have a unique small holomorphic solution under
the same assumptions. All subprincipal symbols contribute only
to subprincipal terms by the connected-edge count.

Move the unmarked invertible matrices \(L_\pm\) to the right
through the finite original word. Conjugation by their
\(\Gamma\)-substitutions is a linear change of creation and
differentiation fields, preserving balancedness and analyticity.
Every relative crossing has the analytic quartic phase just
proved. An independent stage mark \(\Gamma(M(\mathbf t))\),
with \(M(0)=I\), has the exact normal symbol
\[
     \exp\bigl(Z^T(M(\mathbf t)-I)P/h\bigr)
 \tag{27}
\]
in the scaled fields. Its phase is quadratic and \(O(\mathbf t)\),
as allowed above. Finite applications of (25) therefore produce
an analytic balanced principal phase
\(\mathcal P(z,Z,P,\mathbf t)\) for the actual relative word.
At zero marks it is quartic at the origin.

The original pivot is an \(h\)-dependent linear substitution
with matrix \(I+O(h)\). Its relative scaled symbol has exponent
of order \(h^0\), hence no \(h^{-1}\) coefficient. The scalar
framing correction also contributes only to the amplitude.
Both remain in the full formal symbol. The fixed scalar \(x_0^c\)
is retained outside the trace. This construction uses the same
relative word and the same unmarked matrix
\(B=L_\beta(x_0)T_0\) as [C] and [B]; it has not moved \(T_0\)
through an inverse or averaged the cut.

## 5. Applying the calculation to the regular trace contractions

Use the exact covariance decomposition of [C] and [B]:
\[
 \mathcal C(z)=B(I-B)^{-1}=uv^T/z+G(z).
 \tag{28}
\]
The vectors \(u,v\) are the fixed rank-one residue factors;
\(G(z)\) is holomorphic. Substitute the scaled soft fields
\(Z=vA,\ P=uB_s\), and contract the hard fields with covariance
\(hG(z)\). To use (19), order the hard variables as \((Z_h,P_h)\)
and take the symmetric block covariance
\[
             K_G(z)=
              \begin{pmatrix}0&G(z)^T\\G(z)&0\end{pmatrix}.
 \tag{29}
\]
This gives exactly the Wick rule of [B, (7)] after field scaling.
Equations (23)--(24), applied to \(\mathcal P\), prove that its
hard effective principal phase is holomorphic in
\((z,A,B_s,\mathbf t)\).

Balancedness makes it invariant under
\((A,B_s)\mapsto(\lambda A,\lambda^{-1}B_s)\) whenever both
points lie in its disk. Its Taylor coefficients thus have equal
powers of \(A\) and \(B_s\). It is genuinely analytic in
\(x=AB_s\): a bidisk Cauchy bound \(|c_{pq}|\le Mr^{-p-q}\)
gives \(|c_{nn}|\le Mr^{-2n}\). Denote this holomorphic function
by \(\Psi(z,x,\mathbf t)\).

We verify the coefficient correspondence rather than just its
symmetry. The unscaled hard functional is exactly (8) of [B].
Under \(Z,P\mapsto h^{-1/2}Z,h^{-1/2}P\) its hard covariance
becomes \(hG\), and its soft variable becomes \(x=ht\).
The principal coefficient is therefore
\[
       \Psi(z,x,0)=\sum_{j\ge1}u_{j,j+1,0}(z)x^{j+1}.
 \tag{30}
\]
This is the series in [B, (18)].

Before the substitution \(\mathbf t=h m\), the same independent
marks are present in the exact word. The logarithmic contraction
counts above give no powers below \(h^{-1}\). After that
substitution, a term \(h^r\mathbf t^\gamma\) contributes
\(h^{r+|\gamma|}m^\gamma\). Thus the only term of order \(h^0\)
linear in \(m\) comes from differentiating the principal
\(h^{-1}\Psi\) in an independent mark:
\[
       \partial_{t_i}\Psi(z,x,0)
                  =\sum_{j\ge1}u_{j,j,e_i}(z)x^j .
 \tag{31}
\]
Subprincipal terms cannot supply such a coefficient. This is
exactly \(\Theta_i\) in [B], with every original stage or
matching-lattice specialization unchanged.

At zero marks the phase starts at \(x^2\). The calibration
already proved from the actual source in [C, Section 4] gives
\[
 \Psi(z,x,0)=\sigma x^2+O(zx^2,x^3),\qquad
            \partial_{\mathbf t}\Psi(z,x,0)
                            =\mu x+O(zx,x^2).
 \tag{32}
\]
The coefficients here are those of the original cut, not freely
chosen normalizations.

Finally \(\partial_x\Phi_0(0,0)=0\) and
\(\partial_x^2\Phi_0(0,0)=2\sigma\ne0\).
The analytic implicit function theorem gives \(x_g(z,\mathbf t)\)
in (3). Equations (4) follow from (32). The envelope identity
also gives
\[
 \left.\partial_{\mathbf t}
       \Phi_{\mathbf t}(z,x_g(z,\mathbf t))\right|_{\mathbf t=0}
                           =\Theta_g(z).
 \tag{33}
\]
Together with the formal stationary calculation of [B], this
proves the theorem.

## 6. What this changes on the critical path

The phase and its leading clock map are now analytic germs derived
from the literal finite word, even where individual classical
occupation coordinates vanish. Their construction uses small
implicit systems and never divides by those coordinates. It
also avoids the unrelated question whether a formal Hamiltonian
or operator logarithm converges.

The exact soft moment identity of [B] is still a formal endpoint
identity. Turning the present phase into an analytic integral
for the full quantum source would require control of its quantum
amplitude and of the corresponding continuation. Proving that
its nonzero stationary contribution has a nonzero coefficient
in the original physical cycle is a further requirement.
Neither follows just from (4) or from the uniqueness of the
implicit solutions.

Thus this note removes the convergence question for the local
principal phase and leading clock map. It does not identify
their branch with the geometric component of a character
variety, a finite-meridian source minor, or the hyperbolic
volume, and proves no finite-exception theorem.

## 7. Complete direct sources

| Label | Complete written source | SHA256 |
|---|---|---|
| F | notes/research_classical_verma_rational_loops.md | f88f5fc4d1eb0f68f9270e581bd0e1bfd43c669cef989d9813f6000feb4e3659 |
| H | notes/research_actual_source_natural_log_filtration.md | 98c371fe71a210e9d886e30d60a487a3fe46599f1814c1b69229d829a1eb6f88 |
| C | notes/research_actual_clock_finite_core_volterra_carriers.md | 7c7630796cb2d7ee2e81d0efceb9c9008bbb5214169ce4da5b76f068c0341d9a |
| B | notes/research_actual_hard_wick_soft_reduction.md | b528230f79ceea7a9a812ac600bcb55e9ba7819a465218761e0f81fdd317002b |

F supplies the literal entries and original cut; H supplies their
Poisson kernel and formal natural logarithmic filtration. C supplies
the original trace covariance, marks and calibrated soft coefficients.
B supplies the exact formal one-variable reduction and coefficient
definitions matched in (30)--(31). The Poisson and Gaussian implicit
calculations, their analytic solutions, the explicit top potentials,
and the convergence of the principal phase are proved above.

Only written mathematics, source-text reads and hash checks were used.
Frozen manuscripts and public documentation are unchanged.
