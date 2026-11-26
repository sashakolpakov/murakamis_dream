# The original period equations along a chain of powers minus two

The exact marked reduction of a same-sign two-crossing chain already
gives a different description of its filled complement. The
[two-boundary source theorem](research_internal_two_crossing_chain.md)
also retains its canonical polynomial and both boundary normal
derivatives. Neither fact, by itself, says that every cell in the
original unreduced decomposition is positive.

Here the original primitive equations admit an additional exact
simplification. Their half-angle cosines satisfy a linear recurrence.
It gives a regular, correctly charged critical configuration at every
finite length, with strictly negative core signs. Section 12 proves
positivity of all eight original shapes at every edge for all
sufficiently long complete runs. Section 13 retains both outside
values: on its selected long-run branch, every interior block is
positive, and only the two actual attaching blocks need to be checked.
The length thresholds are existential and depend on the specified
compact set of outside values in the latter statement.

Section 10 proves a separate extension for mixed paths. A terminal
power minus two is allowed when its neighbor has magnitude at least
six and every other magnitude is at least three. In this class the
original cells are positive, and the marked-completion theorem gives
the actual hyperbolic filling. General mixed paths still require
control of the neighboring equations and their attaching blocks.

## 1. An invariant of the original degree-two equation

For an edge joining angles \(t_j,t_{j+1}\), put
\[
 C_j=\cos(t_j/2),\qquad a_j=\tan(t_j/2),\qquad
 q_j^2=1+a_j^2+a_{j+1}^2.
 \tag{1}
\]
On the original positive chart, the endpoint return has
\[
 \sinh r_{j,j+1}=a_jC_{j+1},\qquad
 \cosh r_{j,j+1}=q_jC_{j+1}.
 \tag{2}
\]
These identities continue wherever their branches remain regular.
At a degree-two vertex of original power \(-2\), the full primitive
unit-charge equation is
\[
              r_{j,j-1}+r_{j,j+1}=-it_j-\pi i.
 \tag{3}
\]
Define the edge quantity
\[
                 \Lambda_j=C_jC_{j+1}(1+iq_j).
 \tag{4}
\]

**Lemma 1.** Equation (3) implies
\[
 \Lambda_j=\Lambda_{j-1},\qquad
             C_{j+1}=2\Lambda_{j-1}C_j-C_{j-1}.
 \tag{5}
\]
Thus \(\Lambda_j=\Lambda\) is constant along a chain of powers \(-2\).

**Proof.** Write \(r=r_{j,j-1}\). The full charge in (3) gives
\[
 \sinh r_{j,j+1}=\sinh(r+it_j),\qquad
 \cosh r_{j,j+1}=-\cosh(r+it_j).
 \tag{6}
\]
The sign in the second identity is essential. Substitution of (2),
\(\cos t_j=2C_j^2-1\), and \(\sin t_j=2a_jC_j^2\) gives
\[
 C_{j+1}
     =C_{j-1}\{2C_j^2-1+2iq_{j-1}C_j^2\}
     =2\Lambda_{j-1}C_j-C_{j-1}.
 \tag{7}
\]
The second identity in (6) gives
\[
 q_jC_{j+1}
    =-q_{j-1}C_{j-1}(2C_j^2-1)
                        -2iC_{j-1}(1-C_j^2).
 \tag{8}
\]
Adding \(i\) times (8) to (7) and multiplying by \(C_j\)
gives (4) with \(\Lambda_j=\Lambda_{j-1}\).
\(\square\)

The recurrence preserves the quadratic relation
\[
 \Lambda^2-2\Lambda C_jC_{j+1}+C_j^2+C_{j+1}^2=0.
 \tag{9}
\]
Consequently
\[
            q_j=i\left(1-\frac{\Lambda}{C_jC_{j+1}}\right)
 \tag{10}
\]
satisfies (1) whenever the denominator is nonzero.
This also verifies the converse algebra in (6), with its full
sinh and cosh data; using coth alone would lose a further sign.

## 2. Two complete outside ends

Let there be \(k\ge1\) selected vertices, put \(L=k+1\), and
index the two complete outside ends by \(0,L\).
Thus \(C_0=C_L=1\). At the left outside edge the original branch
has \(q_0=1/C_1\), so
\[
                         C_1=\Lambda-i.
 \tag{11}
\]
The recurrence therefore reads
\[
 C_j=T_j(\Lambda)-iU_{j-1}(\Lambda),
 \tag{12}
\]
where \(T_j,U_j\) are the Chebyshev polynomials and \(U_{-1}=0\).

Choose the already proved selected isolated solution of degree
two and positive power \(L\), as in
[the isolated-vertex geometry](research_isolated_internal_vertex_geometry.md).
Write its angle as \(2\beta\). Its full equation is
\[
 2\operatorname{arsinh}(\tan\beta)=iL\beta-\pi i,\qquad
 0<\Re\beta<\pi/L,\quad \Im\beta<0.
 \tag{13}
\]
With \(\varphi=L\beta/2\), its canonical branches satisfy
\[
 \cos\varphi=i\tan\beta,\qquad \sin\varphi=\sec\beta.
 \tag{14}
\]
The first identity follows by taking sinh in (13); the second
follows by squaring and choosing the positive-real branch.
Indeed \(0<\Re\varphi<\pi/2\), so both \(\sin\varphi\) and
\(\sec\beta\) have positive real part.

Set \(\Lambda=\cos\beta\). Then (11)--(12) have the explicit form
\[
 \boxed{\displaystyle
 C_j=\frac{\cos((j-L/2)\beta)}{\cos(L\beta/2)},
                      \qquad 0\le j\le L.}
 \tag{15}
\]
Identity (14) gives \(C_1=\Lambda-i\), and (15) gives both
complete outside values exactly.

## 3. A pendant chain

Now the first selected vertex is an original terminal, and the
only complete outside end is \(L=k+1\). At the terminal the full
equation is \(r_{1,2}=-it_1-\pi i\). Equation (2) then gives
\[
 C_2=2iC_1^2,\qquad q_1C_2=1-2C_1^2,\qquad
                         \Lambda=iC_1.
 \tag{16}
\]
It is convenient to introduce a virtual value \(C_0=0\).
This is not a complete outside cusp; it is simply the initial
value which makes the same recurrence valid at \(j=1\).
We have \(C_1=-i\Lambda\).

Choose the selected isolated terminal solution of positive
power \(L\), again writing its angle as \(2\beta\). Then
\[
 \operatorname{arsinh}(\tan\beta)=iL\beta-\pi i,\qquad
 0<\Re\beta<\pi/L,\quad\Im\beta<0.
 \tag{17}
\]
On these branches,
\[
                  \sin(L\beta)=i\tan\beta,\qquad
                  \cos(L\beta)=-\sec\beta.
 \tag{18}
\]
For the second sign, the first identity has positive imaginary
part, so \(\pi/2<L\Re\beta<\pi\); hence \(\cos(L\beta)\)
has negative real part. The recurrence is consequently
\[
 \boxed{\displaystyle
 C_j=\frac{\sin(j\beta)}{\sin(L\beta)}
          =-i\cos\beta\,U_{j-1}(\cos\beta),
                        \qquad 0\le j\le L.}
 \tag{19}
\]
It has \(C_0=0\), \(C_1=-i\Lambda\), and \(C_L=1\).
The final outside edge also has
\(C_{L-1}=\Lambda-i\), by (18).

## 4. Regularity, signs, and the full primitive charges

**Proposition 2.** In (15) or (19), every selected \(C_j\) lies
strictly in the fourth quadrant. Define
\[
                 t_j=-2\arccos C_j
 \tag{20}
\]
using the branch with
\(0<\Re(\arccos C_j)<\pi/2\) and
\(\Im(\arccos C_j)>0\). Then
\[
                         -\pi<\Re t_j<0,\qquad \Im t_j<0.
 \tag{21}
\]
Every actual edge value (10) has positive real part, and so do
both products \(q_jC_j,q_jC_{j+1}\).
The principal returns
\[
       r_{j,j+1}=\operatorname{arsinh}(a_jC_{j+1})
 \tag{22}
\]
satisfy all the full primitive equations of power \(-2\),
including the original terminal equation when present.

**Proof.** Write \(\beta=x-iy\), with \(x,y>0\).
The number \(\Lambda=\cos\beta\) lies in the first quadrant.
In (15), the argument of
\(\cos(s\beta)\), for \(0\le s\le L/2\), is
\[
                 \arctan(\tan(sx)\tanh(sy)).
 \tag{23}
\]
It is strictly increasing for \(s>0\). The numerator in (15)
uses \(|j-L/2|<L/2\), so its argument is nonnegative and
strictly below the argument of the denominator. This puts each
selected quotient strictly in the fourth quadrant.
Moreover, if \(\alpha=\arg\cos(L\beta/2)\) and
\(\delta=\arg\Lambda\), (14) gives
\[
 \delta+\alpha=\pi/2+\arg\sin\beta<\pi/2,\qquad
                         \delta+2\alpha<\pi.
 \tag{24}
\]
All arguments are in the quadrants just specified, so these
are identities without a hidden multiple of \(2\pi\).

For (19), the argument of \(\sin(s\beta)\) increases strictly
on \(0<s\le L\), because
\[
 \frac{d}{ds}\arg\sin(s\beta)
   =\frac{x\sinh(2sy)-y\sin(2sx)}
           {\cosh(2sy)-\cos(2sx)}>0.
 \tag{25}
\]
The first quotient \(C_1=-i\Lambda\) has argument
\(\delta-\pi/2\). All later selected quotients therefore
have arguments between this value and zero, proving the
same fourth-quadrant statement.

In the corridor case, \(-\alpha\le\arg C_j\le0\), with
\(\delta+2\alpha<\pi\). In the pendant case the corresponding
bound is \(\delta-\pi/2\le\arg C_j\le0\).
Thus, on every actual edge,
\[
               0<\arg\frac{\Lambda}{C_jC_{j+1}}<\pi.
 \tag{26}
\]
Equation (10) proves \(\Re q_j>0\).
The same bounds give
\(0<\arg(\Lambda/C_j)\le\pi/2\). Since
\[
       q_jC_{j+1}=i\left(C_{j+1}-\frac{\Lambda}{C_j}\right),
 \tag{27}
\]
both products in the proposition have strictly positive real
part. The square root in \(\cosh r_{j,j+1}\) is therefore
exactly \(q_jC_{j+1}\), rather than its negative.

Relations (5), (9), and (10) now give both sinh and cosh
identities (6) for the principal returns. Their sum differs
from \(-it_j-\pi i\) by a multiple of \(2\pi i\).
The imaginary parts of the two principal returns lie in
\((-\pi/2,\pi/2)\), while
\(\Im(-it_j-\pi i)=-\Re t_j-\pi\in(-\pi,0)\).
These ranges exclude every nonzero multiple of \(2\pi i\).
At a terminal, (16) gives the same two identities directly,
and the one-return range excludes the same ambiguity.
This proves the full original charges. \(\square\)

There is no zero among the rational face-chart factors
\[
 q_j,\quad q_j\pm i,\quad q_j\pm a_j,\quad q_j\pm a_{j+1},
 \quad a_j\pm i,\quad a_{j+1}\pm i.
 \tag{28}
\]
Indeed \(\Re q_j>0\), while \(1+a_j^2=1/C_j^2\ne0\);
the remaining assertions follow from (1). The original
apex denominators factor through these quantities as in
the marked-completion note. Thus this is a regular critical
configuration, rather than a formal solution created by
canceling a zero denominator.

## 5. What the recurrence does not yet prove

For the original eight-shape edge block, positivity requires
\[
              \Re q_j>
                 \sqrt{(\Re a_j)^2+(\Re a_{j+1})^2}.
 \tag{29}
\]
The weaker signs in Proposition 2 do not imply (29) for an
arbitrary regular edge. A local recurrence can leave the
positive chamber, so positivity cannot be asserted simply
by iterating (5). Section 12 establishes (29) for (15) and (19)
at all sufficiently large lengths. The shorter lengths remain
untreated by that argument. In particular the recurrence alone
is not the positivity proof.

The already proved marked reduction carries the proper rotations,
both boundary crossing shifts, primitive disk frames, and framing.
It can be used to obtain a positive description of the same
filled exterior from the reduced isolated vertex. That description
is a different cell decomposition; it is not a proof of (29).
Mixed chains containing magnitudes two and at least three need a
further argument as well. No new quantum asymptotic is claimed here.

## 6. Where a corner can occur in a mixed negative path

One conclusion from the threshold-three proof does extend to
paths containing magnitude two.

**Proposition 3.** Suppose every selected magnitude in the
negative path is at least two, with the original hypotheses
of the [variational note](research_negative_corridor_variational_bounds.md).
At any corner of its minimum, the endpoint with negative
incidence has magnitude exactly two.

**Proof.** Theorem 6 of that note excludes negative endpoints of
magnitude at least four without assuming larger magnitudes at
their neighbors. Propositions 8--9 likewise apply with all
magnitudes at least two. For a hypothetical magnitude-three
negative endpoint they give
\[
 2\pi/3<\theta<\pi,\qquad \pi/2<\phi<\pi,\qquad
                         2\le n\le6.
\]
Lemma 12 and the outgoing bound still give
\(y<4x/3\), where \(x=\pi-\theta\), \(y=\pi-\phi\).
The exclusions of \(n=3,4,5,6\) in Sections 13--14 use only
these local bounds and the same endpoint KKT equations.
Their proofs do not require a third vertex to have magnitude
at least three.

For \(n=2\), the remaining real equation requires \(F_2(x,y)\ge C_2\).
The two monotonicities (94)--(95), now with \(n=2\) and \(k=4/3\),
give
\[
 F_2(x,y)<\operatorname{arsinh}(4/3)
              -\tfrac12\operatorname{arsinh}(3/4)
              =\log3-\tfrac12\log2<\log3.
 \tag{30}
\]
But
\[
 C_2=\operatorname{arsinh}(1/2)
               +\tfrac12\operatorname{arsinh}2
       >1/\sqrt5+\log2>\log3.
 \tag{31}
\]
For the last inequality use
\(\log(3/2)\le(3/2-1)/\sqrt{3/2}=1/\sqrt6<1/\sqrt5\).
Thus \(n=2\) is impossible as well. Magnitude three cannot be
the negative endpoint, leaving only magnitude two.
\(\square\)

This is a restriction on the location and direction of a possible
corner. It does not prove that a maximal run of magnitudes two
can be removed while preserving positivity of the original cells.
The exact marked reduction and the recurrence above must still be
distinguished from such a positivity-preserving replacement.

## 7. The boundary condition needed for a run replacement

A proposed replacement of a run must control its outside periods.
Regularity, the full internal charges, and positivity at the incoming
edge are insufficient, even for three consecutive powers minus two.
Here is an exact example of that specific failure.

Set
\[
 \Lambda=\frac{43}{50}+\frac{9i}{200},\qquad
 C_0=1,\quad C_1=\Lambda-i,\quad
 C_{j+1}=2\Lambda C_j-C_{j-1}\quad(1\le j\le3).
 \tag{32}
\]
The remaining values are
\[
\begin{split}
 C_2&=\frac{11303}{20000}-\frac{3913}{2500}i,\\
 C_3&=\frac{126463}{500000}-\frac{3372561}{2000000}i,\\
 C_4&=\frac{4329593}{200000000}-\frac{16405489}{12500000}i .
\end{split}
 \tag{33}
\]
Keep \(t_0=0\), and set \(t_j=-2\arccos C_j\) on the branch
in (20). Thus vertices \(1,2,3\) are selected, and vertex \(4\)
is an outside boundary with a fixed complex angle. In particular
\(C_4\ne1\); this is not a complete-boundary example.

Define \(a_j=\tan(t_j/2)\) and \(q_j\) by (10). Every \(C_j\)
with \(j>0\) is strictly in the fourth quadrant. Exact rational
arithmetic gives
\[
 \Re q_j>0,\qquad
 \Re(q_jC_j)>0,\qquad \Re(q_jC_{j+1})>0
                  \quad(0\le j\le3).
 \tag{34}
\]
The argument following (27) therefore applies without change:
the principal returns satisfy all three full equations (3).
All rational face-chart factors in (28) remain nonzero.

Nevertheless, if
\[
 d_j=(\Re q_j)^2-(\Re a_j)^2-(\Re a_{j+1})^2,
 \tag{35}
\]
then
\[
 d_0>\frac{19}{100},\qquad
 d_1>\frac1{40},\qquad
 d_2>\frac1{250},\qquad
 d_3<-\frac1{12500}.
 \tag{36}
\]
Thus the first three original edge blocks are positive and the
fourth is not. This disproves a run-replacement criterion based
only on regular attaching periods and positivity propagated
from one end. It leaves open a criterion using both outside
conditions, including the selected complete-end relations
(14) or (18).

The inequalities are exact algebraic comparisons. Since
\(a_j^2=C_j^{-2}-1\) is a Gaussian rational number,
\[
       (\Re a_j)^2=\frac{|a_j^2|+\Re(a_j^2)}2.
 \tag{37}
\]
The [rational verifier](../experiments/check_negative_two_run_boundary_obstruction.py)
checks the quadratic relation (9), the signs (34), and (36).
It encloses each square root in (37) between consecutive rational
numbers with denominator \(10^{30}\); squaring the endpoints
verifies every enclosure by integer arithmetic. The
[saved output](../repro/results/research-negative-two-run-boundary-obstruction.json)
contains all exact fractions and the verifier's hash. No numerical
root finder is involved.

## 8. The first original edge of a selected pendant chain

The selected endpoint relation does give a uniform positivity
statement at the terminal end.

**Proposition 4.** The edge joining vertices \(1,2\) in the
pendant solution (19) is positive for every \(L\ge2\).

**Proof.** Set \(w=(2\Lambda^2)^{-1}=u-iv\).
The selected values at \(L=2,3\) are respectively
\[
 \Lambda=\frac{1+i}{2},\qquad
 \Lambda=\frac{\sqrt7+i}{4};
\]
these are the isolated terminal solutions used in (17).
They give \(w=-i\) and \(w=(3-i\sqrt7)/4\).
For \(L\ge4\), the bound \(0<\Re\beta<\pi/L\) gives
\[
 \Re(\Lambda^2)
   =\frac{1+\cos(2\Re\beta)\cosh(2\Im\beta)}2>\frac12,
 \qquad \Im(\Lambda^2)>0.
\]
Consequently, in every case,
\[
                  u\ge0,\qquad v>0,\qquad |w|\le1.
 \tag{38}
\]

Since \(C_1=-i\Lambda\) and \(C_2=-2i\Lambda^2\), the
original quantities on this edge obey
\[
        a_1^2=-1-2w,\qquad a_2^2=-1-w^2,\qquad
                         q_1=i(1+w).
 \tag{39}
\]
In particular \(\Re q_1=v>0\). The matrix
\[
       L_1=\begin{pmatrix}q_1+a_1&a_2\\a_2&q_1-a_1\end{pmatrix}
\]
has determinant one, and direct expansion gives
\[
       2\det(\Re L_1)
        =1+|q_1|^2-|a_1|^2-|a_2|^2
        =S-A-B,
 \tag{40}
\]
where \(S=1+|1+w|^2\), \(A=|1+2w|\), and \(B=|1+w^2|\).
This formula also follows by writing the determinant of \(L_1\)
in real and imaginary parts.

Put \(P=S^2-A^2-B^2\). Polynomial expansion yields
\[
\begin{split}
 P&=2(2u+1)(u^2+v^2+1)>0,\\
 P^2-4A^2B^2
   &=-16v^2\{(u^2+v^2)^2-2(u^2+v^2)-4u\}>0.
\end{split}
 \tag{41}
\]
The last sign uses (38): if \(r=u^2+v^2\in(0,1]\),
then \(r^2-2r-4u<0\). Thus \(P>2AB\), whence
\(S>A+B\). Equations (40) and \(\operatorname{tr}(\Re L_1)
=2\Re q_1>0\) show that \(\Re L_1\) is positive definite.
The original edge criterion (29) is exactly that condition.
\(\square\)

This verifies the original terminal block, rather than a block
in the reduced decomposition. The remaining internal edges
require a global argument, supplied for sufficiently long
complete runs in Section 12. Proposition 4 does not supply
the local propagation rule ruled out in Section 7.

## 9. A sufficient comparison using the original return angles

The following criterion isolates a possible global comparison.
It concerns the original cells and does not change their coordinates.

**Lemma 5.** Suppose
\[
 -\pi<\Re t,\Re u<0,\qquad \Im t,\Im u<0,
\]
and take the principal original returns
\[
 r_t=\operatorname{arsinh}(\tan(t/2)\cos(u/2)),\qquad
 r_u=\operatorname{arsinh}(\tan(u/2)\cos(t/2)).
\]
If both imaginary parts are nonpositive, then all eight original
edge shapes are positive.

**Proof.** Write \(C=\cos(t/2)\), \(D=\cos(u/2)\) and
\[
              z=-C^{-2},\qquad w=-D^{-2}.
 \tag{42}
\]
Both \(z,w\) have strictly negative imaginary part. The tangent
squares are \(-1-z,-1-w\), and the original root satisfies
\(q^2=-1-z-w\), with \(\Re q>0\). By the same determinant
identity as in (40), the required positivity is equivalent to
\[
                |1+z+w|+1>|1+z|+|1+w|.
 \tag{43}
\]

Both returns have strictly negative real part. Indeed their
sinh arguments have negative real part, because the tangents
lie in the third quadrant and \(C,D\) in the fourth quadrant.
For \(r=-K+ig\), where \(K>0\) and
\(-\pi/2<g<\pi/2\),
\[
             \Im(\sinh^2r)=-\tfrac12\sinh(2K)\sin(2g).
\]
Thus the assumptions give
\[
 \Im\frac{1+w}{z}\ge0,\qquad
 \Im\frac{1+z}{w}\ge0,
 \tag{44}
\]
since these two quotients are respectively
\(\sinh^2r_u\) and \(\sinh^2r_t\).
With \(J=\Im(\overline z w)\), (44) says
\[
                         \Im z\le J\le-\Im w.
 \tag{45}
\]

Let \(f(s,t)=|1+sz+tw|\) for \(0\le s,t\le1\).
Its argument is never zero: its imaginary part is negative
unless \(s=t=0\), where the argument equals one.
The Hessian of the Euclidean norm gives
\[
 \frac{\partial^2 f}{\partial s\,\partial t}
   =\frac{(-\Im z+tJ)(-\Im w-sJ)}
          {|1+sz+tw|^3}\ge0.
 \tag{46}
\]
Both factors are strictly positive near \((0,0)\), and (45)
makes them nonnegative on the whole square. Integrating (46)
therefore gives the strict inequality (43). \(\square\)

For the selected pendant chain, one of the two incidence signs
on every internal edge follows already from (25). Specifically,
\[
       \Im r_{j,j+1}<0\qquad(1\le j<L-1).
 \tag{47}
\]
To verify this, the arguments of \(C_j\) increase strictly in
\((-\pi/2,0)\), so \(C_{j+1}/C_j\) is in the first quadrant.
Consequently
\[
 \Im\!\left(\frac{C_{j+1}^2}{C_j^2}-C_{j+1}^2\right)>0.
 \tag{48}
\]
The expression in parentheses is \(\sinh^2r_{j,j+1}\);
the sign follows as in the proof of the lemma.

The opposite incidence requires the additional inequality
\[
          \Im\!\left(\frac{C_j^2}{C_{j+1}^2}-C_j^2\right)\ge0.
 \tag{49}
\]
For \(j=1\), (49) equals
\[
 \Im\!\left(\Lambda^2+\frac1{4\Lambda^2}\right)
   =\Im(\Lambda^2)\!
        \left(1-\frac1{4|\Lambda|^4}\right)\ge0
\]
by the selected bound used in Proposition 4. For the other
indices, (49) is a concrete sufficient global comparison.
Section 12 proves it at every index once the complete run
is sufficiently long. Generic regular solutions of the
recurrence do not satisfy it, as Section 7 demonstrates.

## 10. A terminal power two beside a larger negative power

There is a useful exact criterion for an original terminal
power \(-2\), even when the rest of the path is not a chain of
twos. Write \(C_1=\cos(t_1/2)\) at that terminal and
\(C_2=\cos(t_2/2)\) at its neighbor. The terminal equation gives
the same local identities used in Section 8:
\[
              C_1=-i\Lambda,\qquad C_2=-2i\Lambda^2 .
 \tag{50}
\]

**Lemma 6.** Suppose (50) has the selected negative-angle branches
of Section 4, and \(C_2\) lies strictly in the fourth quadrant.
The original terminal edge has all eight shapes positive exactly
when
\[
                       |C_2|^2(1-2\Im C_2)>\frac12 .
 \tag{51}
\]
In particular this edge is positive if
\(-\Re t_2\le\pi/2\).

**Proof.** Put \(w=(2\Lambda^2)^{-1}=-i/C_2=u-iv\).
Now \(u,v>0\), without the additional assumption \(|w|\le1\)
used in Section 8. Both squarings in (40)--(41) are equivalences:
\(S,A,B>0\) and \(P>0\). Hence the determinant is positive
exactly when
\[
                  (u^2+v^2)^2-2(u^2+v^2)-4u<0 .
 \tag{52}
\]
Write \(C_2=\xi-i\zeta\), with \(\xi,\zeta>0\), and
\(R=|C_2|^2\). Then \(u=\zeta/R\), \(v=\xi/R\), and
the left side of (52) is
\((1-2R-4\zeta R)/R^2\). This is exactly (51).
The trace of the real edge matrix is positive, so the positive
determinant is equivalent to positivity of the original shapes.
Finally, if \(t_2=-\phi-2ih\), with \(h>0\) and
\(0<\phi\le\pi/2\), then
\(\Re C_2=\cos(\phi/2)\cosh h\ge1/\sqrt2\).
Thus (51) holds strictly. \(\square\)

This criterion applies to an ordinary regular configuration.
At a corner minimum, a strict subgradient is not such a
configuration. The following argument instead uses the exact
corner optimality equations.

**Proposition 7.** At a corner of a negative path with every
magnitude at least two, suppose the negative-incidence endpoint
is an original terminal of magnitude two. Its real angle
magnitude is greater than \(3\pi/4\), and its neighbor's is
greater than \(\pi/2\). The neighboring magnitude is at most five.

Consequently, a path with every magnitude at least three except
possibly an original terminal of magnitude two has a positive
original-cell solution if that terminal's neighbor has magnitude
at least six. Under the standing complete-outside-end hypothesis,
this is the actual marked hyperbolic filling, with its absolutely
normalized action-volume identity.

**Proof.** Orient a hypothetical corner so that the negative
endpoint is \(v\). Let
\(\theta=-s_v\), \(\phi=-s_w\). The corner incidence is
\(g_{v,e}=-(\pi-\phi)/2\). Since \(v\) is terminal and its
magnitude is two, its filling equation reads
\[
                   g_{v,e}=\theta-\pi,\qquad
                         \phi=2\theta-\pi .
 \tag{53}
\]
In particular \(\pi/2<\theta<\pi\).

Use the corner covectors of Sections 8--9 of the
[variational note](research_negative_corridor_variational_bounds.md):
\[
 \begin{split}
 X&=\tfrac12\operatorname{arsinh}(-\cot\theta\sin\phi)>0,\\
 Y&=\tfrac12\operatorname{arsinh}(\cot\phi\sin\theta),\\
 0&<U<X,\qquad
 V\ge V_0(U):=\tfrac12\operatorname{arsinh}(\operatorname{csch}(2U)).
 \end{split}
 \tag{54}
\]
The terminal real equation, including its original degree one,
is
\[
                             U+X=2(V+Y).
 \tag{55}
\]
If \(\theta\le3\pi/4\), (53) gives \(\phi\le\pi/2\)
and \(Y\ge0\). Put \(\delta=\theta-\pi/2\). Then
\[
       \sinh(2X)=\tan\delta\sin(2\delta)=2\sin^2\delta\le1.
 \tag{56}
\]
It follows that \(V_0(X)\ge X\). The function \(V_0\)
is strictly decreasing, so \(U<X\) gives \(V>V_0(X)\ge X\).
The right side of (55) is therefore greater than \(2X\),
whereas its left side is less than \(2X\), a contradiction.
Thus \(\theta>3\pi/4\) and \(\phi>\pi/2\).

Let \(n\) be the neighboring magnitude. Its corner incidence
is \(g_{w,e}=(\pi-\theta)/2\). If it has a second edge, that
edge's incidence is strictly less than \(\pi/2\): for a
selected neighbor this follows from the edge angle bound and
its strictly positive angle magnitude; for a complete outside
neighbor the incidence is negative. Its filling equation gives
\[
                         n\phi<4\pi-\theta .
 \tag{57}
\]
A terminal neighbor gives the stronger equality
\(n\phi=3\pi-\theta\). Using (53) and the strict lower bound
on \(\theta\) in (57) yields
\[
                  n<\frac{4\pi-\theta}{2\theta-\pi}
                                <\frac{13}{2}.
 \tag{58}
\]
Hence the integer \(n\) is at most six.

We can also exclude \(n=6\), using both endpoints' real equations.
Now \(Y<0\); put \(H=-Y>0\) and \(\delta=\theta-\pi/2\).
The unchanged interior square gives
\[
 X=\tfrac12\operatorname{arsinh}(2\sin^2\delta),\qquad
 H=\tfrac12\operatorname{arsinh}
             \left(\frac{2\sin^2\delta-1}{2\sin\delta}\right).
 \tag{59}
\]
The positive endpoint's core height is \(X-U\). Its corner
return has real part \(-V-H\). Every other return, if present,
has strictly negative real part. Consequently
\[
 n(X-U)\ge V+H,\qquad V=(U+X)/2+H,
\]
and hence
\[
 U\le U_n:=\frac{(2n-1)X-4H}{2n+1},\qquad
 V\le V_n:=\frac{2nX+(2n-1)H}{2n+1}.
 \tag{60}
\]
The first inequality is strict when that endpoint has another
edge, but the weak inequality suffices.

For \(n=6\), (57) gives \(\delta<7\pi/26\). The tangent-line
bound for the concave sine, followed by \(\pi<22/7\), gives
\[
 \sin\delta<
 \sin(\pi/4+\pi/52)
 \le\frac{1+\pi/52}{\sqrt2}
 <\frac{193}{182\sqrt2}<\frac34 .
 \tag{61}
\]
Both \(U_6\) and \(V_6\) increase with \(\delta\) on
\((\pi/4,\pi/2)\). Indeed \(X'>0\) and direct differentiation
of (59) gives
\[
                  \frac{H'}{X'}
                         =\frac12+\frac1{4\sin^2\delta}\in(3/4,1).
 \tag{62}
\]
At the larger comparison value \(\sin\delta=3/4\), the two
functions in (59) are
\(\tfrac12\operatorname{arsinh}(9/8)\) and
\(\tfrac12\operatorname{arsinh}(1/12)\). They satisfy
\[
                X<\frac{121}{250},\qquad
                       \frac1{25}<H<\frac1{24}.
 \tag{63}
\]
For the first bound, the first three terms of the positive
sinh series at \(121/125\) already exceed \(9/8\).
For the lower bound on \(H\), use
\(\operatorname{arsinh}x\ge x/\sqrt{1+x^2}\);
the upper bound follows from \(\operatorname{arsinh}x<x\).
Substitution in (60), and the monotonicity just proved, give
\[
                         U<\frac25,\qquad V<\frac{483}{1000}.
 \tag{64}
\]
For \(0<x\le1\), a geometric bound on the remaining sinh
series gives
\[
 \sinh x\le B(x):=x+\frac{x^3}{6}+\frac{x^5}{120}
                         +\frac{x^7}{4970}.
 \tag{65}
\]
The tail starts at \(x^7/7!\), and its successive ratios are
at most \(1/72\), explaining the denominator \(4970\).
An exact rational multiplication gives
\(B(4/5)B(483/500)<499/500<1\).
Equation (64) therefore contradicts
\(\sinh(2U)\sinh(2V)\ge1\).
This excludes \(n=6\), leaving \(n\le5\).

For the stated class of paths, Proposition 3 says that every
corner would have a negative endpoint of magnitude two.
It would therefore have to be the terminal just treated.
Its neighbor has magnitude at least six, which has just been excluded.
Open square sides were already excluded, so the unique convex
minimum is interior. The strict core signs and the
[pointwise marked-completion theorem](research_positive_point_marked_completion.md)
give the claimed original geometry and volume normalization.
\(\square\)

The new condition concerns an original terminal, whose filling
equation has only one incidence. It does not apply to a
degree-two endpoint adjacent to a complete outside vertex.
Neither Proposition 7 nor the exact local criterion (51)
proves positivity for general internal runs of twos. No
quantum asymptotic is claimed by this section.

The small rational bounds in (61), (63)--(65) can be replayed with
the [exact-arithmetic checker](../experiments/check_terminal_two_corner_bound.py):

    python3 experiments/check_terminal_two_corner_bound.py \
      --output repro/results/research-terminal-two-corner-bound.json

The [saved result](../repro/results/research-terminal-two-corner-bound.json)
records each rational comparison, its positive gap, and the checker
hash. An independent run may use another output path. These six
arithmetic checks verify the displayed constants; the written proof
supplies the monotonicity, corner equations and marked completion.

## 11. Eliminating a run while retaining its two original returns

Consider \(L-1\ge1\) consecutive degree-two vertices of power
\(-2\), between two actual outside vertices numbered \(0,L\).
The outside angles need not be complete. Write
\[
 A=C_0=\cos(t_0/2),\qquad B=C_L=\cos(t_L/2),\qquad
 U=U_{L-1}(\Lambda),\qquad V=U_{L-2}(\Lambda).
 \tag{66}
\]
Here \(U_j\) and \(T_j\) remain the Chebyshev polynomials; the
letter \(V\) in this section denotes a polynomial value, not a
corner covector. Assume the original branch is regular and
satisfies the full primitive equations (3). Lemma 1 supplies
its constant \(\Lambda\).

**Proposition 8.** If \(U\ne0\), every half-angle cosine in the
run is determined by the two boundary values:
\[
 C_j=\frac{A\,U_{L-j-1}(\Lambda)+B\,U_{j-1}(\Lambda)}
                  {U_{L-1}(\Lambda)}
       \quad(0\le j\le L),
 \qquad U_{-1}=0.
 \tag{67}
\]
The remaining conic equation is exactly
\[
 \boxed{\quad
 \Lambda^2U_{L-1}(\Lambda)^2+A^2+B^2
                      -2ABT_L(\Lambda)=0 .
 \quad}
 \tag{68}
\]
The two original endpoint returns retain both their sinh and
cosh, and hence their exponentials:
\[
 \begin{array}{ll}
 \sinh r_{0,1}=a_0 C_1,&
 \cosh r_{0,1}=i(C_1-\Lambda/A),\\
 \sinh r_{L,L-1}=a_L C_{L-1},&
 \cosh r_{L,L-1}=i(C_{L-1}-\Lambda/B),
 \end{array}
 \qquad a_v=\tan(t_v/2).
 \tag{69}
\]
In particular these equations can be substituted into the original
filling equations at the two neighboring vertices. Their other
incidences and primitive charges are unchanged. The logarithmic
lifts must still be retained from the original calibration;
sinh and cosh alone leave a \(2\pi i\) ambiguity.

**Proof.** The recurrence gives
\[
       B=A\,T_L(\Lambda)+U(C_1-\Lambda A)
         =UC_1-VA .
 \tag{70}
\]
Solving for \(C_1\) and propagating the recurrence gives (67).
Multiply the initial conic
\(\Lambda^2-2\Lambda AC_1+A^2+C_1^2=0\)
by \(U^2\). The polynomial identities
\[
 U^2+V^2-2\Lambda UV=1,\qquad
                         \Lambda U-V=T_L(\Lambda)
 \tag{71}
\]
reduce the result to (68). Conversely, (68) with \(U\ne0\)
implies that initial conic, so the recurrence preserves it on
every edge. Formula (10), multiplied by the neighboring cosine,
gives (69). This retains the original ordered endpoint exponentials.
Their full logarithmic lifts are those of the given primitive
solution; the selected comparison below calibrates them explicitly.
\(\square\)

There is no cancellation of the exceptional set \(U=0\) in this
statement. On that set one must keep the homogeneous pair
\[
            UC_1-VA=B,\qquad
       \Lambda^2-2\Lambda AC_1+A^2+C_1^2=0 .
 \tag{72}
\]
Indeed if \(U=0\), then
\(\Lambda=\cos(k\pi/L)\), \(1\le k<L\), and
\(T_L(\Lambda)=(-1)^k=:\epsilon\). Equation (70) becomes
\(B=\epsilon A\); the initial cosine \(C_1\) is still constrained
by the second equation in (72). The eliminated equation (68)
merely reads \((B-\epsilon A)^2=0\), and does not determine
that extra information.

For the negative-angle domain of interest, the exceptional set
has a useful direct exclusion. Suppose every interior \(C_j\)
lies strictly in the fourth quadrant, and both actual endpoint
values have positive real part and nonpositive imaginary part.
Multiply the recurrence by \(\sin(\pi j/L)\) and sum over the
interior vertices. Discrete summation by parts gives
\[
 2\left(\Lambda-\cos\frac{\pi}{L}\right)
       \sum_{j=1}^{L-1}\sin\frac{\pi j}{L}\,C_j
                 =\sin\frac{\pi}{L}\,(A+B).
 \tag{73}
\]
The sum and \(A+B\) have positive real parts and nonpositive
imaginary parts. Their quotient therefore has strictly positive
real part. Consequently
\[
                         \Re\Lambda>\cos(\pi/L).
 \tag{74}
\]
Every root of \(U_{L-1}\) is real and at most \(\cos(\pi/L)\),
so \(U\ne0\) follows. This proves the needed division on that
domain, rather than removing the exceptional factor formally.

### The selected branch and the boundary crossing shifts

Near the selected complete-end solution of Section 2, choose
\(\beta=\arccos\Lambda\) as there and put \(t_*=2\beta\).
The exact endpoint conics give
\[
 \begin{split}
 C_1&=A(\Lambda-iR_A),&
 R_A^2&=1+a_0^2\Lambda^2,\\
 C_{L-1}&=B(\Lambda-iR_B),&
 R_B^2&=1+a_L^2\Lambda^2 .
 \end{split}
 \tag{75}
\]
The roots \(R_A,R_B\) equal one at complete endpoints.
All statements in the following paragraph continue on the
connected regular branch with these choices and with
\(\Lambda\ne0,\pm1\).

Let \(r^{\rm red}_{0,*}=\operatorname{arsinh}(a_0\Lambda)\)
and \(r^{\rm red}_{L,*}=\operatorname{arsinh}(a_L\Lambda)\),
continued from zero at complete endpoints. Substitution in
(69) verifies both the sinh and cosh of the exact identities
\[
 \boxed{\qquad
 r_{0,1}=r^{\rm red}_{0,*}-\frac{i t_0}{2},\qquad
 r_{L,L-1}=r^{\rm red}_{L,*}-\frac{i t_L}{2}.
 \qquad}
 \tag{76}
\]
For example,
\(\sinh(r^{\rm red}_{0,*}-it_0/2)
  =a_0A(\Lambda-iR_A)=a_0C_1\).
Its cosh is
\(A R_A-i\Lambda(1-A^2)/A=i(C_1-\Lambda/A)\).
At complete endpoints both sides vanish, which fixes the
integer logarithmic ambiguity.

The new center obeys the full positive-power-\(L\) equation
\[
       r_{*,0}+r_{*,L}=iL\beta-\pi i .
 \tag{77}
\]
Here \(\sinh r_{*,0}=A\sin\beta/\Lambda\) and
\(\cosh r_{*,0}=A R_A/\Lambda\), and similarly at the other
end. To check (77), write (70) using (75) as
\[
       B/A=\cos(L\beta)-iR_A\frac{\sin(L\beta)}{\sin\beta}.
 \tag{78}
\]
It gives
\(\sinh r_{*,L}=\sinh(r_{*,0}-iL\beta)\).
The reversed recurrence and the second line of (75) give
\(\cosh r_{*,L}=-\cosh(r_{*,0}-iL\beta)\).
These are both exponential identities in (77). Its full
charge is fixed by (13) at the complete point and continued
without changing branches.

Thus a neighboring original power \(-b\) becomes \(-(b-1)\)
in the reduced period equation: inserting (76) into its old
equation moves exactly \(it_v/2\) to the other side. This is
the \(+1\) boundary crossing in the
[exact marked run reduction](research_repeated_two_crossing_chain_reduction.md),
with the proper half-turn, disk frames and primitive curve
shear retained there. Equation (76) does not erase that
half-turn on an arbitrary attached tangle.

There are two qualifications. First, (68) alone cannot select
the primitive charge or the branch in (75). For instance,
\(\Lambda=1\), \(C_j=1-ij\), \(A=1\), \(B=1-iL\)
satisfies the original conic and recurrence, with regular
negative-angle values and the original full internal charges.
But \(2\arccos\Lambda=0\) is not a selected charged center
in (77). To check the original branches directly, for this
example
\[
 \begin{split}
 \Re q_j&=\frac{2j+1}{|C_jC_{j+1}|^2}>0,\\
 \Re(q_jC_{j+1})&=j+1+\frac{j}{1+j^2}>0,\\
 \Re(q_jC_j)&=j+\frac{j+1}{1+(j+1)^2}>0.
 \end{split}
 \tag{79}
\]
Thus the principal sinh and cosh branches match (6), and
their ranges give the original full charges exactly as in
Proposition 2. All the face factors in (28) are nonzero.
In fact every original edge in this example is positive. The
first edge has positivity margin
\((\Re q_0)^2-(\Re a_1)^2=(3-\sqrt5)/4>0\).
For \(j\ge1\), the two return-sign expressions of Lemma 5 are
\[
 \begin{split}
 \Im\left\{(C_j/C_{j+1})^2-C_j^2\right\}
   &=2j+\frac{2(1+j(j+1))}{(1+(j+1)^2)^2}>0,\\
 \Im\left\{(C_{j+1}/C_j)^2-C_{j+1}^2\right\}
   &=2\left\{j+1-\frac{1+j(j+1)}{(1+j^2)^2}\right\}>0.
 \end{split}
 \tag{80}
\]
For the last sign, multiply by \((1+j^2)^2\); the numerator
inside braces is \(j^2(j^3+j^2+2j+1)>0\).
Both principal returns therefore have negative imaginary part,
and Lemma 5 applies. The far boundary here is the specified
complex value \(1-iL\), not a complete outside cusp.
This is a degeneration of the reduced chart even though the
original run and both its end edges are positive.

Second,
the endpoint and primitive equations do not prove positivity
of every original edge. That still requires (29), or a
separate criterion such as (49). The formulas supply exact
composable boundary data. The selected long-run positivity
theorem in Section 13 adds a separate estimate and explicitly
retains its two attaching-block tests. Neither statement is a
quantum-cycle assertion.

The [boundary-return checker](../experiments/check_negative_two_run_boundary_returns.py)
can be run with

    .venv/bin/python experiments/check_negative_two_run_boundary_returns.py \
      --output repro/results/research-negative-two-run-boundary-returns.json

It checks the polynomial recurrence and elimination identities
symbolically for \(2\le L\le20\). Six selected complex boundary
germs are then checked at 90 decimal digits, including the full
internal charges, both endpoint-return shifts and (73). It also
replays the regular original branch with \(\Lambda=1\).
The [saved result](../repro/results/research-negative-two-run-boundary-returns.json)
records the errors and checker hash. These are supplementary
checks of the general written identities, not a positivity or
asymptotic test.

## 12. Positivity for every sufficiently long complete run

The complete-end condition is enough to prove a uniform result in
the length. It is important here to estimate all indices in a run
at once. Pointwise convergence with a fixed index would leave the
middle of an increasingly long run untreated.

**Theorem 9.** There is an integer \(L_0\) such that, for every
\(L\ge L_0\), all original edge blocks in each of the following
configurations have eight positive shapes:

1. the two-ended corridor (15), with \(C_0=C_L=1\);
2. the pendant chain (19), with its original terminal equation
   and \(C_L=1\).

The angles, face maps, primitive charges, and outside markings are
the original ones in Sections 1--4. In particular the
[marked-completion theorem](research_positive_point_marked_completion.md)
applies to these configurations. This theorem gives an existential
length threshold; no numerical value of \(L_0\) is asserted.

### The selected parameter as the length increases

We first record bounds common to the two cases. Put \(d=2\) for
the corridor and \(d=1\) for the pendant chain. Their selected
equations are
\[
 d\,\operatorname{arsinh}(\tan\beta)=iL\beta-\pi i.
 \tag{81}
\]
In both cases,
\[
 \beta=\frac{\pi}{L}-\frac{d\pi i}{L^2}+O(L^{-3}),
 \qquad
 \Lambda=1-\frac{\pi^2}{2L^2}
                  +\frac{d\pi^2 i}{L^3}+O(L^{-4}).
 \tag{82}
\]
Here and below each \(O\)-constant is independent of the index
of a vertex. Only \(d=1,2\) occur.

For completeness, the small parameter in (82) is the already
selected solution, rather than another root of the exponentiated
equation. Write \(\beta=x-iy\), where \(x,y>0\), and
\(a=(\pi-Lx)/d\). On the branches of (13) or (17),
\[
 \tanh(Ly/d)=\frac{\sin x}{\cosh y},
       \qquad \tan a=\frac{\sinh y}{\cos x}.
 \tag{83}
\]
These follow by taking tanh in (81) and using
\(\tanh(\operatorname{arsinh}(\tan\beta))=\sin\beta\);
the real and imaginary parts select \(0<a<\pi/2\).
Since \(0<x<\pi/L\), the first identity gives
\[
 0<y\le \frac dL\operatorname{artanh}(\sin x)
       =\frac dL\operatorname{arsinh}(\tan x)=O(L^{-2}).
\]
Thus \(L\beta\to\pi\). With \(\epsilon=L^{-1}\) and
\(\beta=\epsilon z\), (81) becomes
\[
 d\,\operatorname{arsinh}(\tan(\epsilon z))=iz-\pi i.
\]
Its derivative in \(z\) at \((\epsilon,z)=(0,\pi)\) is
\(-i\ne0\). The implicit-function theorem gives
\(z=\pi-d\pi i\epsilon+O(\epsilon^2)\), proving (82) for
the selected branch. In particular there are positive absolute
constants \(c,C\), which may change between estimates, such that
for all sufficiently large \(L\),
\[
 \frac cL\le x\le\frac{\pi}{L},\qquad
 \frac c{L^2}\le y\le\frac C{L^2}.
 \tag{84}
\]
In the pendant case write \(\cot\beta=p+iq\). Then
\[
 cL\le p\le CL,\qquad c\le q\le C,\qquad
 \frac qp=\frac{\sinh(2y)}{\sin(2x)}\ge\frac yx.
 \tag{85}
\]

### Pendant chains: the indices away from either end

Put
\[
 F_j=iC_j=\cot\beta\,\sin(j\beta),\qquad F_L=i,
 \qquad
 H_j=\Im\left\{F_j^2+\left(\frac{F_j}{F_{j+1}}\right)^2\right\}.
 \tag{86}
\]
Thus \(H_j\) is precisely the missing comparison (49).
The other incidence sign is already (47).
We will prove, with constants independent of \(L,j\),
\[
 \begin{array}{ll}
 \Im(F_j^2)\ge c j^4/L^3,&
 \left|\Im\{(F_j/F_{j+1})^2\}\right|\le Cj/L^3,
                         \quad 1\le j\le L/2,\\[2mm]
 \Im(F_j^2)\ge c(L-j),&
 \left|\Im\{(F_j/F_{j+1})^2\}\right|\le C/(L-j)^2,
                         \quad L/2\le j\le L-2 .
 \end{array}
 \tag{87}
\]
The real and imaginary parts of \(F_j\) are
\[
 \begin{split}
 \Re F_j&=p\sin(jx)\cosh(jy)
                         +q\cos(jx)\sinh(jy),\\
 \Im F_j&=q\sin(jx)\cosh(jy)
                         -p\cos(jx)\sinh(jy).
 \end{split}
 \tag{88}
\]
For \(j\le L/2\), all trigonometric factors here are
nonnegative. Equations (84)--(85) give
\(\Re F_j\ge cj\). Moreover,
\[
 \begin{split}
 \Im F_j
 &\ge p\cosh(jy)
       \left\{\frac yx\sin(jx)-\cos(jx)\tanh(jy)\right\}\\
 &\ge \frac{py}{x}\{\sin(jx)-jx\cos(jx)\}
 \ge c\,j^3/L^3 .
 \end{split}
 \tag{89}
\]
The last inequality follows from
\(\sin z-z\cos z=\int_0^z t\sin t\,dt\ge 2z^3/(3\pi)\)
for \(0\le z\le\pi/2\).
This proves the first lower bound in (87).

For \(j\ge L/2\), put \(s=L-j\). The identity
\(\pi-jx=(\pi-Lx)+sx\), together with (82)--(84),
gives
\[
 \sin(jx)\ge cs/L,\qquad
 \Re F_j\ge cs-C/L\ge c's
                      \quad(2\le s\le L/2).
 \tag{90}
\]
Also \(\Im F_j\ge c\), uniformly in this range. To see this
without discarding a possible sign, first take
\(L/2\le j\le3L/4\). Then \(\sin(jx)\) is bounded below,
while \(\cos(jx)\le C/L^2\); the second, possibly negative,
term in the second line of (88) is \(O(L^{-2})\).
For \(j\ge3L/4\), \(\cos(jx)\le-c\), so that same term
is positive and at least \(cpjy\ge c'\).
This proves the second lower bound in (87).

For the ratio estimates, set
\[
 m_j=\frac{F_j}{F_{j+1}}
                 =\frac{\sin(j\beta)}{\sin((j+1)\beta)}.
\]
An exact product-to-sum calculation gives
\[
 -\Im m_j=
 \frac{\sin x\,\sinh((2j+1)y)
                   -\sin((2j+1)x)\sinh y}
      {\cosh(2(j+1)y)-\cos(2(j+1)x)}.
 \tag{91}
\]
For \(j\le L/2\), put \(k=2j+1\). The numerator is
\[
 y\{k\sin x-\sin(kx)\}
 +\sin x\{\sinh(ky)-ky\}
 -\sin(kx)\{\sinh y-y\}.
\]
The elementary bounds
\(|\sin z-z|\le |z|^3/6\) and
\(|\sinh z-z|\le C|z|^3\) on the present bounded ranges
give an absolute bound \(Cj^3/L^5\).
The denominator is at least \(c(j+1)^2/L^2\).
Consequently \(|\Im m_j|\le Cj/L^3\).
Furthermore \(|m_j|\le C\), since
\[
 |\sin(j\beta)|^2=\sin^2(jx)+\sinh^2(jy)
\]
and the same denominator bound applies. This proves the
first ratio estimate in (87).

For \(j\ge L/2\), the numerator in (91) is at most \(C/L^2\).
With \(s=L-j\ge2\), its denominator is at least
\[
 2\sin^2((j+1)x)\ge c(s-1)^2/L^2\ge c's^2/L^2 .
\]
The numerator of \(m_j\) has absolute value at most \(Cs/L\);
its denominator has absolute value at least \(cs/L\).
Thus \(|m_j|\le C\) and \(|\Im m_j|\le C/s^2\),
giving the second ratio estimate in (87).
In both cases we used
\(|\Im(m_j^2)|\le2|m_j|\,|\Im m_j|\).

It follows from (87) that there is a fixed integer \(K\)
such that
\[
                  H_j>0\quad\hbox{if }K\le j\le L-K .
 \tag{92}
\]
The integer \(K\) is independent of \(L\). This is the
uniform estimate needed for the middle of the run.

### Pendant chains: the finitely many end indices

For each fixed \(j\ge1\), the expansion of
\(F_j(\Lambda)=\Lambda U_{j-1}(\Lambda)\) at \(\Lambda=1\)
gives
\[
 H_j=
 \frac{2\pi^2j^2}{3L^3}
 \left\{j^2+2-\frac{2j+1}{(j+1)^2}\right\}
       +O_j(L^{-4}).
 \tag{93}
\]
Indeed \(F_j(1)=j\),
\(F_j'(1)=j(j^2+2)/3\), and
\[
 \left(\frac{U_{j-1}}{U_j}\right)'(1)
                   =-\frac{j(2j+1)}{3(j+1)} .
\]
The coefficient in braces in (93) is strictly positive.
This treats each of the finitely many indices \(j<K\).

At the other end, fix \(s=L-j\ge2\).
The two exact selected identities (18) give
\[
 F_{L-s}=U_{s-1}(\Lambda)+iT_s(\Lambda)\longrightarrow s+i .
 \tag{94}
\]
Therefore
\[
 H_{L-s}\longrightarrow
       2s-\frac{2(s(s-1)+1)}{((s-1)^2+1)^2}>0 .
 \tag{95}
\]
For the last strict sign, put \(r=s-1\ge1\).
After multiplication by the positive denominator and division
by two, the numerator is
\[
 (r+1)(r^2+1)^2-\{r(r+1)+1\}
                     =r^2(r^3+r^2+2r+1)>0.
\]
This treats the finitely many \(2\le s<K\).
The remaining index \(s=1\) has \(H_{L-1}=0\) exactly,
because \(F_L=i\). It is the edge meeting the complete
outside cusp.

Taking the maximum of the finitely many length thresholds in
(93)--(95) and the threshold in (92) proves (49) on every
internal edge for all sufficiently large \(L\).
Lemma 5 and (47) prove positivity of these original blocks.
The edge meeting the complete cusp is positive directly:
with \(a=\tan(t/2)\) and \(q=\sec(t/2)\),
\[
 q+a=\tan(\pi/4+t/4),\qquad
 q-a=\cot(\pi/4+t/4)
\]
have positive real parts when
\(-\pi<\Re t<0\), \(\Im t<0\).
Thus \(\Re q>|\Re a|\), which is (29) at that edge.

### Two-ended corridors

The same division into a middle interval and fixed end indices
works here, with a simpler middle estimate. Write
\[
 D=\cos(L\beta/2)=i\tan\beta,\qquad
 N_j=\cos((j-L/2)\beta),\qquad C_j=N_j/D .
\]
The corridor expansion (82), now with \(d=2\), gives
\[
 \Re D\asymp L^{-2},\qquad
 \Im D\asymp L^{-1},\qquad |D|^2\asymp L^{-2}.
 \tag{96}
\]
The symbol \(\asymp\) means bounds above and below by
positive constants independent of \(L,j\).
We claim that, with \(s_j=\min(j,L-j)\),
\[
       \Re C_j\ge c,\qquad
       -\Im C_j\ge cs_j,\qquad
       |C_j|\le C(s_j+1)
                   \quad(1\le j<L).
 \tag{97}
\]
By symmetry it suffices to take \(j\le L/2\) and put
\(h=L/2-j\). Both parts of
\[
          N_j=\cos(hx)\cosh(hy)
                         +i\sin(hx)\sinh(hy)
\]
are nonnegative. If \(j\ge L/4\), its real part is bounded
below, and the term
\(\Re N_j\,\Re D/|D|^2\) proves \(\Re C_j\ge c\).
If \(j\le L/4\), its imaginary part is at least \(c/L\),
and \(\Im N_j\,\Im D/|D|^2\) gives the same conclusion.
Also
\[
 \Re N_j\ge cj/L,\qquad \Im N_j\le C/L .
\]
The first inequality uses
\(\cos(hx)=\sin((\pi-Lx)/2+jx)\).
Consequently
\[
 -\Im C_j
 =\frac{\Re N_j\,\Im D-\Im N_j\,\Re D}{|D|^2}
                    \ge cj-C/L\ge c'j .
\]
Finally \(\Re N_j\le C(j+1)/L\) and
\(\Im N_j\le C/L\), proving the upper bound in (97).

If \(s_j,s_{j+1}\ge K\), (97) bounds both adjacent ratios
\(|C_j/C_{j+1}|\) and \(|C_{j+1}/C_j|\) by an absolute
constant. On the other hand
\[
        -\Im(C_j^2)=2\Re C_j(-\Im C_j)\ge cs_j .
\]
After increasing \(K\), both expressions
\[
 \Im\{(C_j/C_{j+1})^2-C_j^2\},\qquad
 \Im\{(C_{j+1}/C_j)^2-C_{j+1}^2\}
 \tag{98}
\]
are strictly positive throughout the middle interval.
They are the two return-sign tests in Lemma 5.

For each fixed \(j\), (12) and \(\Lambda\to1\) give
\(C_j\to1-ij\). For \(j\ge1\), both expressions (98)
then have the strictly positive limits computed in (80).
Only finitely many \(j<K\) remain, and symmetry treats the
right end. The two complete outside edges are positive by
the direct calculation following (95).
This proves the corridor assertion and completes the proof
of Theorem 9. \(\square\)

All primitive equations used in this proof were established
before positivity in Proposition 2. The completion theorem
therefore applies without a change of cells or an inferred
logarithmic charge. It gives the actual partially filled
marked manifold, its complete remaining cusps, and the
absolute volume from the original stationary action.
For each fixed sufficiently long run, positivity and the
nondegenerate period Jacobian also give its local boundary
deformation on the original marking.

The theorem does not give a boundary disk uniform in \(L\),
does not cover an arbitrary prescribed complex value at a far
end, and does not prove a quantum contribution survives.
It also leaves the finitely many shorter lengths untreated
by this argument. Thus it is a geometric result about
complete pure runs, not a theorem for all mixed negative
paths or a new cofinite statement about twist assignments.

## 13. Long runs with both boundary values retained

The middle estimate for corridors has a useful extension. The
outside values need not be complete, provided their half-angle
cosines remain in a fixed compact part of the fourth quadrant.
In this statement the two attaching blocks must be checked; the
theorem proves positivity of all the blocks between them.

**Theorem 10.** Let \(\mathcal K\) be a compact subset of
\[
             \{z\in\mathbb C:\Re z>0,\ \Im z\le0\}.
 \tag{99}
\]
For \(A,B\in\mathcal K\) and all sufficiently large integers
\(L\), uniformly over these boundary values, there is a unique
solution near \(\pi/L\) of
\[
 \operatorname{arsinh}(A\tan\beta)
       +\operatorname{arsinh}(B\tan\beta)
                        =iL\beta-\pi i.
 \tag{100}
\]
Use the small principal branches on the left, set
\[
 \begin{split}
 \Lambda&=\cos\beta,\qquad
 S_A=\sqrt{\,1+(A^2-1)\sin^2\beta\,},\quad S_A\longrightarrow1,\\
 C_j&=A\cos(j\beta)
             -iS_A\frac{\sin(j\beta)}{\sin\beta}
                  \quad(0\le j\le L).
 \end{split}
 \tag{101}
\]
Then \(C_0=A\), \(C_L=B\). All selected angles
\(t_j=-2\arccos C_j\), \(1\le j<L\), have
\(-\pi<\Re t_j<0\), \(\Im t_j<0\), and satisfy the original
full power-\(-2\) equations (3). Every original block with
\[
                         1\le j\le L-2
 \tag{102}
\]
is positive. The two blocks excluded from (102) are precisely
the attaching blocks \((0,1)\) and \((L-1,L)\).
Consequently, on this selected long-run branch, the entire run
is positive if and only if both attaching blocks are positive.
The two original endpoint-return identities (76), with their
logarithmic calibration and primitive curve shifts, still hold.

This is a uniform assertion on \(\mathcal K^2\), not on all
possible complex boundary values. It concerns the small
solution of (100); an arbitrary regular solution of (68)
need not lie on that branch.

**Proof.** Put \(\epsilon=1/L\) and \(\beta=\epsilon z\).
The equation in \(z\) at \(\epsilon=0\) has the simple root
\(z=\pi\). The holomorphic implicit-function theorem, with
parameters \(A,B\) in a bounded neighborhood of \(\mathcal K\),
gives uniformly
\[
 \begin{split}
 \beta&=\frac{\pi}{L}
           -\frac{i\pi(A+B)}{L^2}+O_{\mathcal K}(L^{-3}),\\
 \Lambda&=1-\frac{\pi^2}{2L^2}
           +\frac{i\pi^2(A+B)}{L^3}+O_{\mathcal K}(L^{-4}).
 \end{split}
 \tag{103}
\]
In particular \(\Im\Lambda>0\).
To check the right boundary exactly, write
\(r_A=\operatorname{arsinh}(A\tan\beta)\) and
\(r_B=\operatorname{arsinh}(B\tan\beta)\).
Their cosh values are \(S_A/\Lambda,S_B/\Lambda\).
Equation (100) gives
\[
 B\tan\beta
   =\sinh(r_A-iL\beta)
   =A\tan\beta\cos(L\beta)
                       -i(S_A/\Lambda)\sin(L\beta).
 \]
After multiplication by \(\Lambda/\sin\beta\), this is
exactly \(B=C_L\). The initial values
\(C_0=A\), \(C_1=A\Lambda-iS_A\) satisfy (9);
the recurrence therefore preserves the original conic.

We next prove estimates uniform in the index.
For \(0\le\alpha\le1\), define the real functions
\[
 f(\alpha)=\frac{\sin(\pi\alpha)}{\pi},\qquad
 g_B(\alpha)=f(\alpha)-\alpha\cos(\pi\alpha),\qquad
 g_A(\alpha)=f(\alpha)+(1-\alpha)\cos(\pi\alpha).
 \tag{104}
\]
The subscripts indicate the boundary coefficients in the next
formula; these functions do not themselves depend on \(A,B\).
Expanding (101) using (103) gives, for \(\alpha=j/L\),
\[
 C_j=-iL f(\alpha)+A g_A(\alpha)+B g_B(\alpha)
                                  +O_{\mathcal K}(L^{-1}),
 \tag{105}
\]
uniformly for every \(0\le j\le L\).
Indeed \(j(\beta-\pi/L)=O_{\mathcal K}(L^{-1})\);
the quadratic errors in the sine and cosine expansions are
\(O_{\mathcal K}(L^{-2})\), and
\[
 (\sin\beta)^{-1}=L/\pi+i(A+B)/\pi+O_{\mathcal K}(L^{-1}),
 \qquad S_A=1+O_{\mathcal K}(L^{-2}).
 \]
These bounds justify the uniform remainder in (105).

The functions in (104) satisfy
\[
 g_A(\alpha)=g_B(1-\alpha),\qquad
 g_B(0)=0,\qquad
 g_B'(\alpha)=\pi\alpha\sin(\pi\alpha).
 \tag{106}
\]
Thus they are nonnegative, and \(g_A+g_B\) has a strictly
positive minimum on \([0,1]\).
Writing \(A=a-ih\), \(B=b-ik\), we have \(a,b\ge c>0\)
and \(h,k\ge0\). It follows from (105) that
\[
 \Re C_j\ge c,\qquad
 -\Im C_j\ge c\min(j,L-j),\qquad
 |C_j|\le C\{\min(j,L-j)+1\}
                 \quad(1\le j<L).
 \tag{107}
\]
Here all constants are uniform on \(\mathcal K^2\).
For the imaginary lower bound use
\(f(\alpha)\ge(2/\pi)\min(\alpha,1-\alpha)\).
This proves the claimed angle signs.

The conic root is still (10).
Each interior \(C_j\) has argument at least
\(-\pi/2+c/L\), while \(\arg\Lambda=O_{\mathcal K}(L^{-3})>0\).
The endpoint arguments stay a fixed distance above
\(-\pi/2\). Consequently
\[
             0<\arg\frac{\Lambda}{C_jC_{j+1}}<\pi .
 \]
Thus \(\Re q_j>0\).
Also \(\Im(\Lambda/C_j)>0\), since \(\Re\Lambda>0\),
\(\Im\Lambda>0\), \(\Re C_j>0\), and \(\Im C_j\le0\).
Equation (27) now proves positivity of both real cosh
factors. The sinh and cosh identities (6), and the
principal ranges used in Proposition 2, prove every
original full internal charge. This argument does not
yet assume positivity of the edge shapes.

As in (98), estimates (107) make both return-sign
expressions strictly positive when both endpoints of an
edge are at distance at least a fixed integer \(K_0\)
from \(0,L\). The integer \(K_0\) can be chosen uniformly
on \(\mathcal K^2\).
For a fixed left-end index, (101) instead gives
\[
                           C_j\longrightarrow A-ij .
 \tag{108}
\]
Every edge of this limiting half-chain with \(j\ge1\)
has both return-sign expressions strictly positive.
Here is the exact check, which does not assume that the
attaching edge \(j=0\) is positive. Put
\(H=h+j\ge1\), so the two values are
\(a-iH,a-i(H+1)\). The expressions are
\[
 \begin{split}
 &2a\left\{H+
       \frac{a^2+H(H+1)}{(a^2+(H+1)^2)^2}\right\}>0,\\
 &2a\left\{H+1-
       \frac{a^2+H(H+1)}{(a^2+H^2)^2}\right\}>0 .
 \end{split}
 \tag{109}
\]
For the second inequality its numerator, after division by
\(2a\) and multiplication by the positive denominator, is
\[
 (H+1)a^4+\{2H^2(H+1)-1\}a^2
                        +H(H+1)(H^3-1)>0 .
 \]
Each of the finitely many \(1\le j<K_0\) therefore has a
positive minimum over \(A\in\mathcal K\).
Uniform convergence in (108) preserves those signs for
large \(L\). Reversing the run gives the same argument
with \(B\) at the other end.
Lemma 5 now proves positivity of every edge in (102).

Finally, (101) is (75) with \(A R_A=S_A\), and the
reversed formula gives \(B R_B=S_B\).
The same sinh and cosh calculation therefore proves (76).
For the logarithmic lift, fix the original outside angles
in the closed negative-angle strip with cosines \(A,B\).
At \(\Lambda=1\), the proposed left return is
\[
 \operatorname{arsinh}(\tan(t_0/2))-it_0/2 .
 \]
Its imaginary part lies strictly between
\(-\pi/2\) and \(\pi/2\): the first summand has imaginary
part in \((-\pi/2,0]\), and the added imaginary part is
between \(0\) and \(\pi/2\).
The endpoints with a real half-angle cosine follow by
continuity on the same original branches.
The exact cosh has positive real part by the preceding
argument. Hence this is the original principal return.
The same bounds hold uniformly on a compact boundary
set and persist for large \(L\), proving the full
logarithmic identities without an added \(2\pi i\).
Their primitive-marking interpretation is the exact
one already established after (78). \(\square\)

The theorem supplies a test for long maximal runs inside a
larger negative path. One must solve the retained endpoint
equations, keep those solutions in a fixed compact set (99),
and check the two actual attaching blocks. The theorem then
proves positivity of every original interior block of the
run. It neither solves the neighboring filling equations
automatically nor asserts that their attaching blocks must
be positive. If those remaining equations and blocks are
verified, the original full periods above allow direct use
of marked completion; there is no lost boundary variable
or changed primitive slope.
