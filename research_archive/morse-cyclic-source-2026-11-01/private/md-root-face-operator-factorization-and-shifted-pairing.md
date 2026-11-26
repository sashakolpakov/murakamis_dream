# A factorization of the root face operator and its shifted coefficient identities

The statements here are exact finite algebra at the prescribed root.
They retain the physical endpoints and the original face targets.
They do not prove a norm bound, a spectral gap, or cancellation of a
sewn Green contribution.

## 1. The polynomial space and the source sign

Let \(N\ge2\), \(d=N-1\), \(\theta=\pi/N\), and
\(q=e^{i\theta}\). Write
\[
 s_j=2\sin(j\theta)=\frac{q^j-q^{-j}}{i},\qquad
 c_j=q^{2j+1}+q^{-2j-1}.
 \tag{1}
\]
Define operators on the full polynomial ring by
\[
 Df(z)=\frac{f(qz)-f(q^{-1}z)}{iz},\qquad
 Zf(z)=zf(z),\qquad Tf(z)=f(qz).
 \tag{2}
\]
The numerator in \(D\) vanishes at zero, so this is polynomial.
In particular \(Dz^j=s_jz^{j-1}\), with \(D1=0\).
Here \(T\) denotes the shift only; the old source note's face
operator called \(T\) will be denoted \(\mathsf T_{\mathrm{src}}\).

The coefficient ring may include any other face variables, on
which \(D,Z,T\) act trivially. The actual root face operator in
[the small-circle kernel](/Users/sasha/volume-conjecture/notes/actual_resummed_small_circle_face_kernel.md)
is
\[
 \mathsf T_{\mathrm{src}}z^j
 =-c_jz^j+s_j^2(x+y)z^{j-1}
                   +s_js_{j-1}xy z^{j-2}.
 \tag{3}
\]
Thus the operator on which the original Casimir polynomial acts is
\(\mathsf C=-\mathsf T_{\mathrm{src}}\), not
\(\mathsf T_{\mathrm{src}}\). Terms with negative exponents in (3)
are zero; their sine coefficients already vanish.

The exact factorization is
\[
 \boxed{\displaystyle
 \mathsf C(x,y)=c_0I-D(Z+xI)(Z+yI)D.}
 \tag{4}
\]
Indeed the product on the right sends \(z^j\) to
\[
 s_js_{j+1}z^j+s_j^2(x+y)z^{j-1}
                         +s_js_{j-1}xy z^{j-2},
 \tag{5}
\]
and
\[
 c_0-s_js_{j+1}
 =2\cos\theta-4\sin(j\theta)\sin((j+1)\theta)
 =2\cos((2j+1)\theta)=c_j.
 \tag{6}
\]
These are identities on the full polynomial ring, not just on the
first \(N\) monomials.

## 2. The quotient and both endpoints

Let
\[
                 \mathcal A_N=\mathbb C[z]/(z^N).
 \tag{7}
\]
All three operators in (2) preserve the ideal \((z^N)\), and hence
act on \(\mathcal A_N\). More precisely,
\[
 D(z^Nf)=-z^NDf,\qquad
 T(z^Nf)=-z^NTf,\qquad
 \mathsf C(z^Nf)=z^N\mathsf Cf.
 \tag{8}
\]
The first two signs follow from \(q^N=-1\); the two copies of
\(D\) in (4) cancel the first sign. In particular it would be
incorrect to say that \(D\) commutes with multiplication by
\(z^N\).

In the quotient \(Z\) means truncated multiplication:
\(Zz^d=0\). Formula (4) remains exact with that convention. At
the bottom, \(D1=0\). At the top, the only prematurely truncated
term in the displayed composition is the \(z^N\) term of
\((Z+x)(Z+y)Dz^d\). Its next derivative is zero even on the
full ring, since \(s_N=0\). Thus there is no missing top-row
correction. This is also an immediate consequence of the ideal
invariance in (8).

For a full spectator polynomial with degree exceeding \(d\),
reduction modulo \(z^N\) may be performed before these operators
and the final coefficient extraction. The reason is ideal
invariance, not an assumed bound on spectator degree. In a
multivariable source one may likewise reduce modulo each
ordinary-face power \(L_f^N\). All polynomial multiplications,
shifts, and the corresponding root derivatives preserve those
ideals.

These assertions are at the root. If \(q\) moves away from
\(e^{\pi i/N}\) with the original cutoff \(N\) fixed, the zero
\(s_N=0\), the ideal invariance, and the identities derived from
it need not persist. They cannot be differentiated as if they
were generic-\(q\) identities.

## 3. The coefficient pairing and exact integration

Define
\[
 \phi(P)=[z^d]P,\qquad
              \langle f,g\rangle=\phi(fg).
 \tag{9}
\]
This is a nondegenerate symmetric **bilinear** pairing on
\(\mathcal A_N\). Its matrix in \(1,z,\ldots,z^d\) is the
anti-diagonal matrix of ones. It is not a Hermitian inner
product or a positive norm.

Both \(D\) and \(Z\) are self-adjoint for (9):
\[
       \langle Df,g\rangle=\langle f,Dg\rangle,\qquad
       \langle Zf,g\rangle=\langle f,Zg\rangle.
 \tag{10}
\]
For \(D\), a nonzero monomial pairing requires \(j+k=N\);
then \(s_j=s_{N-j}=s_k\). The endpoint cases give zero on
both sides. For \(Z\), either pairing is the coefficient of
\(z^d\) in \(zfg\), and the truncated terms cannot contribute.
The two middle factors in (4) commute, so (10) also makes
\(\mathsf C\), and every polynomial in it, self-adjoint.

For **every** polynomial, without a degree restriction,
\[
                        \phi(DP)=0.
 \tag{11}
\]
The only possible contributing input coefficient is
\([z^N]P\), and its multiplier is exactly \(s_N=0\).
Equation (11) is a coefficient identity, not a claim that
\(DP=0\).

The actual product rule is
\[
              D(fg)=(Df)(Tg)+(T^{-1}f)(Dg).
 \tag{12}
\]
It follows by adding and subtracting \(f(q^{-1}z)g(qz)\)
in (2), or by the monomial identity
\[
                     s_{j+k}=s_jq^k+q^{-j}s_k.
 \tag{13}
\]
All formulas descend to the quotient. Combining (11) and
(12) gives the shifted integration identity
\[
       \phi\bigl((Df)(Tg)\bigr)
          =-\phi\bigl((T^{-1}f)(Dg)\bigr).
 \tag{14}
\]
Its sign is consistent with the **positive** adjoint sign in
(10). Indeed \(DT^{-1}=q^{-1}T^{-1}D\) and
\[
 \phi(T^{-1}P)=q^{-d}\phi(P)=-q\,\phi(P).
 \tag{15}
\]
Apply (14) with \(g\) replaced by \(T^{-1}g\); its two minus
signs cancel and give (10). Equivalently the shift adjoint is
\(T^*=q^dT^{-1}=-q^{-1}T^{-1}\).

The ordinary derivative rule would be false. For example, put
\(f=z\) and \(g=z^d\). The true terms in (14) sum to
\[
       s_1q^d+q^{-1}s_d=0,
 \tag{16}
\]
whereas the unshifted proposed sum is
\(\phi((Df)g+fDg)=2s_1\ne0\).
This example has the exact root endpoints; it is not an
asymptotic error.

## 4. What is transported onto the other shared factors

For an ordered finite product \(G=G_1\cdots G_m\), iteration
of (12) gives
\[
 DG=\sum_{r=1}^m
       \left(\prod_{j<r}T^{-1}G_j\right)
       (DG_r)
       \left(\prod_{j>r}TG_j\right).
 \tag{17}
\]
The factors commute as polynomials, so another chosen ordering
gives an equivalent total identity. It does not permit the
shifts in a particular summand to be omitted.

In a shared-face source, \(G_j\) is the original factor at its
other incident crossing or triangle, with every occurrence of
the face variable \(z\). Thus \(TG_j\) means replacing that
shared variable by \(qz\) in the entire factor, while retaining
all other face variables and the original spectral data.
It is not a scalar multiple unless that factor happens to be
a monomial in \(z\). The full source commonly has many such
nonmonomial factors.
Moreover, at a different crossing the same face may occupy an
outer position rather than a middle position. Its derivative
in (17) is still the derivative of that entire original factor;
it is not automatically the other crossing's middle-face
Casimir action.

Writing \(A(z)=(z+x)(z+y)\), equations (4),(10) give the exact
second-order integration formula
\[
 \begin{split}
 \phi((\mathsf C F)G)
 &=c_0\phi(FG)-\phi\bigl(A(DF)(DG)\bigr)\\
 &=c_0\phi(FG)
   -\sum_{r=1}^m\phi\left(
       A(DF)(DG_r)
       \prod_{j<r}T^{-1}G_j
       \prod_{j>r}TG_j\right).
 \end{split}
 \tag{18}
\]
It is also \(\phi(F\mathsf CG)\). For a Green equation
\((\sigma I-\mathsf C)F=B\), one may move the operator onto
the **whole** \(G\), but this produces
\((\sigma I-\mathsf C)G\), not an eigenvalue times \(G\).
Equation (18) records the residual terms before any estimate.

Specializing a protected **outer** face to zero only replaces
\(A(z)\), for example by \(z(z+x)\). It does not annihilate
the bilinear term in (18). At \(N=3\), with \(F=G=z\), one
has \(s_1^2=3\) and
\[
       [z^2]\,z(z+x)(DF)(DG)=3.
 \tag{19}
\]
This elementary example is not a claim about a sewn invariant;
it shows why the outer zero by itself is insufficient.

If instead \(z\) is a protected face, its original target is
zero, not \(d\). Then \([z^0]DP=s_1[z^1]P\) need not vanish.
Consequently (11)–(18), with \(\phi=[z^d]\), cannot be
reused at a protected face by silently changing the coefficient
functional. Protected specializations in other variables commute
with the displayed identities.

It follows that this factorization alone does not cancel a
protected-pair Green bulk in a sewn source. The first-order
current involves shifted spectators, and the second-order
current involves (18). A further full-source identity would
have to match those terms with their actual shifts and targets.
No such matching is supplied merely by (4) or (11).

## 5. Relation to the original homogeneous kernel

For a polynomial coupon \(p(\Omega)\), the original homogeneous
face kernel is
\[
 H_p(x,b,c,y)
    =\sum_{j=0}^d \bigl[p(\mathsf C_b)b^j\bigr]c^{d-j}.
 \tag{20}
\]
This is exactly the convention of
[the homogeneous Casimir source](/Users/sasha/volume-conjecture/notes/actual_homogeneous_casimir_face_source.md),
where the operator was written \(p(-\mathsf T_{\mathrm{src}})\).
Each application of \(D\) lowers ordinary polynomial degree by
one, while \((z+x)(z+y)\) raises the total face degree by two.
Thus \(\mathsf C\) preserves total degree in \(x,y,z\), and
every summand of (20) has total degree \(d\). This is distinct
from the degree in one shared spectator variable, which may
be much larger before its target is extracted.
For \(R\) original boxes the product has total degree \(Rd\).
The full marked source extracts degree \(d\) at each of its
\(R\) ordinary faces and degree zero at its two protected faces.
There is no replacement of those targets by a trace in every
face. The four faces at a simple matched quadrilateral are
distinct, so the outer coefficients \(x,y\) in (4) are
independent of its middle variable \(z\).

The identity kernel is \(\sum_{j=0}^db^jc^{d-j}\), and
\[
 [c^d]\,H_p(x,b,c,y)f(c)=p(\mathsf C_b)f(b)
                              \pmod{b^N}.
 \tag{21}
\]
Self-adjointness further gives
\(H_p(x,b,c,y)=H_p(x,c,b,y)\). These are root polynomial
identities retaining all polynomial coupon data, including
Hermite information when a coupon is specified that way.
They do not replace the physical face-grid and mark proof:
the latter is what identifies (20) with the original tensor
entry and the global ordinary targets.

## 6. Existing Ward currents and the scope of this lemma

[The common-band Ward note](/Users/sasha/volume-conjecture/notes/actual_matching_graph_common_band_ward_current.md)
propagates the original Hopf \(E,F,K\) generators through the
typed tensor source, using a primitive **head** lattice.
Its currents are unit translations of internal head
coordinates, with all coproduct prefix characters, charged
bands, physical support cycles, and endpoint differences.
In its generic source coefficients the missing root endpoint
arrows are deliberately not substituted before taking a
normal derivative.

The present \(D\) is instead a root operator on a **face
polynomial**, with the coefficient pairing (9) and the
multiplicative shift \(z\mapsto qz\). The common-band theorem
does not state (4), and its Hopf currents are not automatically
the terms in (17). Relating them would require the literal
face/head transform and its endpoint and normal data.

The root derivative itself, including its high-degree zero
bands, already appears in
[the protected-Green derivative note](/Users/sasha/volume-conjecture/notes/research_green_q_derivative_real_root_structure.md).
That result correctly retains the original cutoff and its
moment-domain obstruction. The factorization and coefficient
adjoints here do not remove either obstruction.

Thus the precise new algebraic conclusion is (4) together with
the root quotient, pairing, and shifted product identities.
There is no claimed positivity, norm comparison, exponential
gap, generic-\(q\) derivative theorem, or automatic cancellation
of the fully sewn Green source.

## 7. The two nilpotent operators generate the full matrix algebra

The exact root commutator is
\[
                    DZ-qZD=s_1T^{-1}.
 \tag{22}
\]
For \(j<d\), this is
\(s_{j+1}-qs_j=s_1q^{-j}\). At \(j=d\) the truncated
\(DZ\) term is zero and
\(-qs_d=s_1q^{-d}\), since \(s_d=s_1\) and \(q^N=-1\).
Thus (22) also retains the top row.

The diagonal clock \(T^{-1}\), with distinct eigenvalues
\(q^{-j}\), lies in the unital algebra generated by \(D,Z\).
Its Lagrange projectors are
\[
 \Pi_j=\prod_{\substack{0\le k\le d\\k\ne j}}
       \frac{T^{-1}-q^{-k}I}{q^{-j}-q^{-k}} .
 \tag{23}
\]
They are the individual degree projectors. Hence
\(Z\Pi_j=E_{j+1,j}\) for \(j<d\), and
\(D\Pi_j=s_jE_{j-1,j}\) for \(j>0\). All \(s_j\) in
this range are nonzero. Products of these adjacent units and
the \(\Pi_j\) give every matrix unit. Therefore
\[
        \mathbb C\langle D,Z\rangle
                  =\operatorname{End}_{\mathbb C}(\mathcal A_N).
 \tag{24}
\]
Although \(D^N=Z^N=0\), they are not simultaneously
triangularizable for \(N\ge2\). Their generated algebra is
the full matrix algebra, not a nilpotent transport algebra.
This statement concerns these two root face operators only;
it makes no assertion about a different source module,
torsor, or asymptotic transport construction.
It also does not say that the original source realizes every
word in \(D,Z\) as an independent physical operation.

## 8. Finite reproduction and the separate sewn-current calculation

The [exact reproduction script](/private/tmp/md-audit-root-face-operator.py)
and [its results](/private/tmp/md-root-face-operator-results.json)
check \(N=2,\ldots,12\), with 6,688 equalities or specified
nonvanishing checks. Arithmetic is integral in
\(\mathbb Z[r]/(r^{2N}+1)\), with \(q=r^2\) and \(i=r^N\).
Evaluation at \(r=e^{\pi i/(2N)}\) gives the required root
exactly. The checks include the full-polynomial and truncated
factorization, high-degree ideal behavior, both coefficient
adjoints, product and integration identities, and the top-row
clock relation. The general proofs above do not depend on
these finite levels.

A separate [shared-source computation](/private/tmp/md-cyclic-signed-global-current-check.py),
with its [frozen results](/private/tmp/md-cyclic-signed-global-current-results.json),
tests the proposed disappearance of a sewn current on the
literal six-box opposite-offset bipyramid at \(N=3\).
For spectra \((2,0,2,2,2,2)\), it finds
\[
 Z=910845,\qquad Z_{\mathrm{north},I}=115587,\qquad
 Z_{\mathrm{south},I}=243.
\]
Writing \(s=0,t=2\) and
\(\chi_3(\sigma)=\sigma^3-3\sigma+2\), the cleared current is
\[
 (s-t)Z-\chi_3(s)Z_{\mathrm{north},I}
                 +\chi_3(t)Z_{\mathrm{south},I}
                         =-2051892 .
\]
The script also obtains the same integer by inserting the
original \(\mathsf C V\) factor at each of the two boxes and
subtracting after the full shared coefficient extraction.
This is a separate obstruction to a claimed exact vanishing
identity. It is consistent with the shifted spectator terms
in (18); it is not a counterexample to an exponential
full-minus-CROSS bound, and it evaluates no filled volume.
