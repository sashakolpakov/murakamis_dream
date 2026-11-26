# A real negative factorial argument at a positive primitive star

Private written proof, 15 November 2026.

Positive primitive geometry does not force the canonical Newton
factorial arguments into their original strip. For every integer
central power \(n\ge5\), a sufficiently large fixed degree admits
an original positive star whose two-leaf multiplication gate has
a real argument \(x+y-z\) strictly between \(-1\) and \(0\).
The outside angles are prescribed and noncomplete. This is not
an exhibited knot exterior or a complete global filling.

All leaves in the construction are identical. Consequently every
binary multiplication tree in the resolution that leaves one factor
for the final pairing and puts all crossings after the products
contains this gate. No assertion is made about redistributing
crossings among proper subproducts.

## 1. An exact positive star with its primitive period

Fix \(n\in\mathbb Z\), \(n\ge5\), and put
\[
 \theta=\frac{2\pi}{n}\in(0,\pi/2),\qquad
 t=\theta-iH,\qquad a=\tan(t/2),\qquad
 r=\frac{nH}{2d},\qquad H>0.
 \tag{1}
\]
Here \(d\ge3\) will be a fixed integer. At each of the \(d\)
outside endpoints choose
\[
 w=a\,\operatorname{csch}r,\qquad
 b=\sqrt{w^2-1}\quad(\Re b>0),\qquad
 q=a\coth r,\qquad u=2\arctan b.
 \tag{2}
\]
The inverse tangent is its canonical branch with
\(|\Re u|<\pi\). In fact \(\Re a>0,\ \Im a<0\), so
\(\Re w>0,\ \Im w<0\); the square root in (2) has positive
real part and negative imaginary part. All these functions
are regular near any fixed \(H>0\).

These are positive configurations of the original edge block.
To prove this directly, write \(w=X+iY\), \(X>0\). Then
\[
 (\Re\sqrt{w^2-1})^2
       =\frac{|w^2-1|+X^2-Y^2-1}{2}<X^2,
 \tag{3}
\]
because
\[
                  (|w|^2+1)^2-|w^2-1|^2=4X^2>0.
 \tag{4}
\]
Also
\[
 q^2=1+a^2+b^2,\qquad \Re q>0,\qquad
 (\Re q)^2-(\Re a)^2=(\Re w)^2>(\Re b)^2.
 \tag{5}
\]
The original positive-edge criterion
\(\Re q>\sqrt{(\Re a)^2+(\Re b)^2}\) therefore holds strictly.
It proves positivity of all eight original edge tetrahedra,
with the canonical branches. In particular no new geometric
edge model is being substituted.

The return at the central endpoint is exactly \(r\). Indeed,
\[
                 \frac{q+a}{q-a}=e^{2r}.
 \tag{6}
\]
The canonical return satisfies
\(e^{2r_t}=(q+a)/(q-a)\) and \(|\Im r_t|<\pi/2\);
since \(r>0\) is real, (6) fixes \(r_t=r\).
Thus the full central marked period is
\[
                   \sum_{e=1}^d r_e-\frac{int}{2}
                    =dr-\frac{in(\theta-iH)}2
                    =-\pi i .
 \tag{7}
\]
This is the primitive equation with the literal integer power
\(n\), not only its exponentiated version. Once \(H\) is chosen,
all outside angles \(u\) in (2) are held fixed. They are
noncomplete: \(b\ne0\), since \(w\) has nonzero imaginary part.
No primitive equations are imposed at those outside endpoints.

## 2. The actual two-leaf prefix labels

Allocate no crossing to the first products. The original prefix
dictionary gives the two identical input labels and their output:
\[
 x=y=\frac1\pi\arctan\!\left(\frac{\tanh r}{a}\right),
 \qquad
 z=\frac1\pi\arctan\!\left(\frac{\tanh(2r)}{a}\right).
 \tag{8}
\]
For large \(d\), these are the analytic inverse-tangent branches
near zero; no integer lift is reset. They correspond to the
returns \(r,r,2r\), respectively. The two-leaf set is proper
when \(d\ge3\).
Their branch also agrees with continuation from positive real
labels: for \(R>0\) and \(\Re a>0,\ \Im a\le0\), the argument
\(\tanh R/a\) has positive real part, and the inverse tangent
is analytic there with its value fixed on the positive real
axis. This gives the stated lift without crossing either
inverse-tangent pole.

Write
\[
 \Delta_d(H)=2x-z,\qquad f(H)=\frac1a+\frac1{a^3}.
 \tag{9}
\]
Taylor expansion of the analytic functions at \(r=0\) gives,
uniformly for \(H\) near any fixed positive value,
\[
 \frac1\pi\arctan\!\left(\frac{\tanh r}{a}\right)
    =\frac{r}{\pi a}-\frac{r^3}{3\pi}
                         \left(\frac1a+\frac1{a^3}\right)
                        +O(r^5),
 \qquad
 \Delta_d(H)=\frac{2r^3}{\pi}f(H)+O(r^5).
 \tag{10}
\]
The remainders and their fixed derivatives are uniform there.

## 3. A transverse real negative value

Put \(c=\cos\theta>0\) and \(s=\sin\theta>0\). The exact expression
\[
 \frac1a=A+iB
       =\frac{s+i\sinh H}{\cosh H-c}
 \tag{11}
\]
has \(A,B>0\). Consequently
\[
 \begin{split}
 \Im f(H)
   &=B(1+3A^2-B^2)\\
   &=\frac{2B\{2-c^2-c\cosh H\}}
                         {(\cosh H-c)^2}.
 \end{split}
 \tag{12}
\]
It has exactly one positive zero, namely
\[
                  H_0=\operatorname{arcosh}(2/c-c)>0.
 \tag{13}
\]
At that zero,
\[
 A=\frac{c}{2s},\qquad B^2=1+3A^2,\qquad
 \Re f(H_0)=-2A(1+4A^2)=-\frac{c}{s^3}<0,
 \tag{14}
\]
and differentiating (12) gives
\[
          \left.\frac{d}{dH}\Im f(H)\right|_{H_0}
                  =-\frac{c^2(4-c^2)}{4s^4}<0.
 \tag{15}
\]

**Theorem.** For every fixed integer \(n\ge5\), and every
sufficiently large fixed integer \(d\), there is
\[
                  H_d=H_0+O_n(d^{-2})
 \tag{16}
\]
for which the original positive primitive star (1)--(7) has
\[
 \boxed{\quad
 \Delta_d(H_d)\in(-1,0),\qquad
 \Delta_d(H_d)=
   -\frac{n^3H_0^3\cos\theta}{4\pi\sin^3\theta}\,d^{-3}
                                  +O_n(d^{-5}).
 \quad}
 \tag{17}
\]

**Proof.** Regard \(\delta=1/d\) temporarily as a real parameter,
with \(r=nH\delta/2\). The quotient
\[
                   F(\delta,H)=\frac{\pi\Delta_d(H)}{2r^3}
 \tag{18}
\]
has a removable extension at \(\delta=0\). It is real analytic
in \((\delta,H)\) near \((0,H_0)\), and (10) gives
\(F(\delta,H)=f(H)+O_n(\delta^2)\). By (12)--(15),
the real equation \(\Im F(\delta,H)=0\) has a unique nearby
real solution \(H(\delta)=H_0+O_n(\delta^2)\).
This is the real implicit-function theorem with nonzero
\(H\)-derivative (15).

At that solution \(\Re F<0\) for small positive \(\delta\),
by (14). Substituting \(r=nH(\delta)\delta/2\) and (14)
in (10) proves (17). Now take \(\delta=1/d\) for every
sufficiently large integer \(d\). The choices of \(n,d,H_d\)
are fixed before any quantum level \(N\) tends to infinity.
Positivity and the complete central period were already
proved exactly in (5)--(7). \(\square\)

All the other arguments of this multiplication gate remain
nonreal with positive imaginary part. Indeed \(x\), \(z\),
\(2x\), and \(z-x\) have respective leading terms
\[
       \frac r\pi(A+iB),\quad
       \frac{2r}\pi(A+iB),\quad
       \frac{2r}\pi(A+iB),\quad
       \frac r\pi(A+iB),
 \tag{19}
\]
with \(B(H_0)>0\). The only real argument among its seven
factorial arguments is the negative \(\Delta_d(H_d)\).
It is noninteger, so this does not contradict the proper-prefix
sine exclusions.

## 4. Source and resolution scope

The original gate is
\[
 \mu_N(Nx,Ny,Nz)=
 \frac{G_N(N(x+y))G_N(Nz)}
 {G_N(Nx)G_N(Ny)G_N(N(z-x))G_N(N(z-y))
                                      G_N(N(x+y-z))}.
 \tag{20}
\]
Its last argument at (17) belongs to the real chamber
\((-1,0)\), with denominator multiplicity \(-1\).
The exact factorial chamber formula therefore retains the
factor
\[
                  1-e^{\tau2\pi iN\Delta_d(H_d)}
 \tag{21}
\]
for either indicated continuation side \(\tau=\pm1\), together
with the corresponding marked action and nonzero local
remainder. This factor is not an asymptotically constant unit
on a neighborhood of that real point. Equation (17) by itself
does not assert that it vanishes at that fixed point for any
particular level.

For the leave-one-factor resolution with all crossing layers
after the products, the \(d-1\) multiplication inputs are
identical copies of (8). Every full binary tree with at least
two leaves has an internal vertex whose two children are
leaves: take a deepest internal vertex. Hence every such
binary parenthesization contains exactly the two-leaf gate
analyzed above. Reassociation within this specified resolution
does not remove it. Redistributing crossings before products
changes the prefix returns and is not covered by this assertion.

The example concerns an original positive edge star with a
primitive central filling and prescribed noncomplete outside
angles. It does not exhibit an actual knot exterior realizing
those angles, or a globally filled knot. It rules out inferring
the original factorial strip solely from positive primitive
geometry, even in this simple boundary problem. The chamber
formula retains the relevant Fourier factor; no obstruction
to a complete corrected contour proof or to the volume identity
is inferred.

## Direct sources

* [Positive edge geometry](research_positive_edge_global_monotonicity.md),
  SHA256
  \(\texttt{da5129c7110190035eedb8249d4004dd06b5a7555e78d948234d8de50fa17500}\):
  original eight-shape positivity criterion, canonical returns
  and branches, and the full marked primitive equation.
* [Positive primitive prefixes](research_positive_primitive_prefix_regularity.md),
  SHA256
  \(\texttt{a01b55a71d133aadff4aac0929e50de03e1059991d6874e81646c770eb5604a6}\):
  exact prefix label dictionary and the specified leave-one
  algebraic resolution.
* [Newton factorial chamber atlas](research_newton_factorial_chamber_atlas.md),
  SHA256
  \(\texttt{34d6e0e4e82a98bf8e6063558ecafdedb0a58d6229fbe462e7e4bfff48f4db4c}\):
  literal gate factorials and the retained real-chamber multiplier.

All arguments are written analytic and algebraic proofs. No
mathematical code, numerical evaluation, tests or compilation
are used.
