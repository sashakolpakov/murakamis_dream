# The literal cyclic Clebsch–Gordan basis and normalized pentagon

Let \(N>2\) be odd, let \(\omega\) be a primitive \(N\)-th root,
and interpret halves in \(\mathbb Z/N\mathbb Z\). We prove the
recoupling and pentagon from the explicit Clebsch–Gordan maps in
[K, (1.13),(1.14)]. Their normalization is retained throughout.
Neither the printed recoupling nor the printed pentagon is assumed.

## 1. The common representation frame and the literal maps

Write \(X|j\rangle=|j+1\rangle\) and
\(Z|j\rangle=\omega^j|j\rangle\). All finite indices are cyclic.
For roots \(P,Q,B\ne0\) satisfying
\[
                    B^N=P^N+Q^N,
\]
put \(d=N-1\) and
\[
 \nu(P,Q)^2=\langle B,Q\rangle
       =\frac{P^N}{N(B-Q)}.
                                                        \tag{1}
\]
Choose one square root for each ordered pair and use that same root
in both its map and its dual. Work on a lifted regular parameter
domain where these choices are holomorphic. The expression in (1)
is nonzero.

For \(x^N+y^N=z^N\), with \(xyz\ne0\), use the finite products
\[
 W(x,y,z;n)=\prod_{j=1}^{[n]}\frac{y}{z-x\omega^j},\qquad
 \overline W(x,y,z;n)=W(x/\omega,y,z;n).
                                                        \tag{2}
\]
They are nonzero and periodic. The bar is a label, not complex
conjugation. The cyclic recurrence extends these formulas to every
integer, including arguments crossing zero.

The specified maps are
\[
 \begin{split}
 (K_\alpha(P,Q))_{ij,k}
 &=\nu(P,Q)\,
   \omega^{\alpha j+\alpha^2/2}
   W(Q,P,B;i-\alpha)\,\delta_{k,i+j},\\
 (K^\alpha(P,Q))_{k,ij}
 &=\frac{\nu(P,Q)}{B^d}\,
   \omega^{-\alpha j-\alpha^2/2}
   \overline W(Q,P,B;i-\alpha)^{-1}\delta_{k,i+j}.
 \end{split}                                             \tag{3}
\]
These are exactly [K, (1.13),(1.14)], after expanding the Gaussian
in the two-index \(w\).

The phrase “in particular basis” in that definition requires a frame
check. The standard representation in [K, (1.6)] is
\(D=P X,E=Z^{-1}\), with
\[
 \Delta E=E\otimes E,\qquad
 \Delta D=1\otimes D+D\otimes E.
\]
The common periodic Gaussian matrix
\[
 G|j\rangle=\omega^{-j(j-1)/2}|j\rangle
\]
satisfies \(GXG^{-1}=XZ^{-1}\). Thus the frame used by (3) is
\[
                         D=P XZ^{-1},\qquad E=Z^{-1}.
                                                        \tag{4}
\]
It is an actual change of basis on every representation, with no
change in its scalar root. Oddness of \(N\) makes the Gaussian
periodic.

There is a short direct intertwining check. Set
\(D'=DE^{-1}\), \(E'=E^{-1}\). In (4), these are \(P X,Z\), and
\[
             \Delta D'=D'\otimes1+E'\otimes D'.
\]
The \(E'\) equation is the delta in (3). The \(D'\) equation is
precisely
\[
 B W(Q,P,B;i-\alpha)
 =P W(Q,P,B;i-1-\alpha)
       +Q\omega^{i-\alpha}W(Q,P,B;i-\alpha),           \tag{5}
\]
which is the recurrence of (2). Since \(D=D'E'^{-1}\) and
\(E=E'^{-1}\), this proves the original two generator equations
as well. One may conjugate (3) back by the same \(G\)'s to use the
standard frame; all recoupling coefficients below are unchanged.

## 2. Complete inverse bases, including the cyclic seam

For \(n=\beta-\alpha\), direct multiplication in (3), on input
index \(k\), gives
\[
 (K^\alpha K_\beta)_{kk}
 =\frac{\nu(P,Q)^2}{B^d}\,
   \omega^{nk+n^2/2}
   \sum_{t\in\mathbb Z/N}\omega^{-nt}
      \frac{W(Q,P,B;t-n)}{\overline W(Q,P,B;t)}.
                                                        \tag{6}
\]
The expression is diagonal in \(k\). For \(1\le[n]<N\), cancellation
of the cyclic products gives
\[
 \frac{W(Q,P,B;t-n)}{\overline W(Q,P,B;t)}
   =\frac{B-Q}{P^{[n]}}
        \prod_{j=1}^{[n]-1}(B-Q\omega^{t-j}).          \tag{7}
\]
After multiplication by \(\omega^{-nt}\), every power in this
polynomial has a nonzero frequency modulo \(N\). Its sum is zero.
For \(n=0\), the ratio is
\((B-Q)/(B-Q\omega^t)\), and its sum is
\[
                  \frac{N B^d(B-Q)}{P^N}.            \tag{8}
\]
For example, (8) follows by multiplying the finite geometric series
by \(B^N-Q^N=P^N\). The prefactor (1) makes (6) equal to one when
\(n=0\). We have proved
\[
 K^\alpha K_\beta=\delta_{\alpha\beta}I_B,
             \qquad \sum_\alpha K_\alpha K^\alpha=I_{P\otimes Q}.
                                                        \tag{9}
\]
The second equality follows because the combined column map has
\(N^2\) columns and rows and the combined dual is its left inverse.
Equations (7),(8) are also the raw orthogonality calculation in
[B, Section 3]. No nondegeneracy or duality assertion is substituted
for this finite calculation. The dual maps intertwine because (9)
and the already proved column intertwining imply their generator
equations.

## 3. Two finite contiguous identities

We will need only finite sums, not a transformation theorem. Define
\[
 v(x;k)=\prod_{j=1}^{k}(1-x\omega^j)^{-1},\qquad
 f(x,y\mid z)=\sum_{k=0}^{N-1}\frac{v(x;k)}{v(y;k)}z^k,
 \qquad z^N=\frac{1-x^N}{1-y^N}.                      \tag{10}
\]
Assume \(x^N,y^N\ne1\) and all other displayed denominators are
nonzero. Extend \(v\) by its recurrence. The summand in (10) is
periodic even though its two separate products need not be.

Write that summand as \(a_k\). Its exact recurrence is
\[
 (1-x\omega^{k+1})a_{k+1}
             =z(1-y\omega^{k+1})a_k.
\]
Summing cyclically gives the first identity
\[
 (1-z)f(x,y\mid z)=(x-\omega yz)f(x,y\mid\omega z).
                                                        \tag{11}
\]
Also
\[
 v(x/\omega;k)=\frac{1-x\omega^k}{1-x}v(x;k),
\]
so
\[
 f(x/\omega,y\mid z)
     =\frac{f(x,y\mid z)-x f(x,y\mid\omega z)}{1-x}.
\]
Using (11) and replacing \(x\) by \(\omega x\) proves
\[
 f(\omega x,y\mid z)
   =\frac{(1-\omega x)(x-yz)}{z(x-y)}f(x,y\mid z).
                                                        \tag{12}
\]
These are identities of the literal finite sums. They do not require
dividing by \(f\). We will telescope them only through nonzero
rational multipliers.

## 4. The actual four-map coefficient

For three objects use roots
\[
 P^N=z_p,\quad Q^N=z_q,\quad R^N=z_r,\qquad
 B^N=P^N+Q^N,\quad C^N=Q^N+R^N,\quad
 H^N=P^N+Q^N+R^N,                                    \tag{13}
\]
all nonzero. Choose the same roots and pair normalizations wherever
the corresponding object occurs. Define the two tree columns
\[
 \begin{split}
 L_{\alpha\beta}&=(K_\alpha(P,Q)\otimes I_R)K_\beta(B,R),\\
 M_{\gamma\delta}&=(I_P\otimes K_\delta(Q,R))K_\gamma(P,C),
 \end{split}
\]
and their literal inverse rows by reversing these products and using
the dual maps in (3). Both are complete bases by (9).

Their coefficient is fixed by the four actual maps:
\[
 \mathscr R_{\alpha\beta}^{\gamma\delta} I_H
      =M^{\gamma\delta}L_{\alpha\beta},\qquad
 L_{\alpha\beta}
      =\sum_{\gamma,\delta}
             \mathscr R_{\alpha\beta}^{\gamma\delta}M_{\gamma\delta}.
                                                        \tag{14}
\]
The first composite is scalar: it intertwines \(E=Z^{-1}\), so it
is diagonal; intertwining \(D=H XZ^{-1}\) makes all its diagonal
entries equal. This uses the actual maps and does not choose an
unspecified basis in a multiplicity space.

For clarity, on physical indices \(i,j,k\), the two columns have
the explicit kernels
\[
 \begin{split}
 L_{\alpha\beta}(i,j,k;l)
 &=\nu(P,Q)\nu(B,R)\,
  \omega^{\alpha j+\beta k+(\alpha^2+\beta^2)/2}
  W(Q,P,B;i-\alpha)W(R,B,H;i+j-\beta)\delta_{l,i+j+k},\\
 M_{\gamma\delta}(i,j,k;l)
 &=\nu(Q,R)\nu(P,C)\,
  \omega^{\delta k+\gamma(j+k)+(\delta^2+\gamma^2)/2}
  W(R,Q,C;j-\delta)W(C,P,H;i-\gamma)\delta_{l,i+j+k}.
 \end{split}                                             \tag{15}
\]
In their four-map contraction the dependence on \(l\) is the factor
\(\omega^{(\beta-\gamma-\delta)l}\) times a sum independent of \(l\).
Scalarity therefore makes the coefficient zero unless
\(\beta=\gamma+\delta\). On that support put
\(n=\gamma-\alpha\), \(u=i-\gamma\), \(v=j-\delta\). Directly
collecting every phase and normalization gives
\[
 \mathscr R_{\alpha\beta}^{\gamma\delta}
 =\frac{\nu(P,Q)\nu(B,R)\nu(Q,R)\nu(P,C)}{C^dH^d}
   \omega^{\alpha\delta+\alpha^2/2}
   S_n\,\delta_{\beta,\gamma+\delta},                 \tag{16}
\]
where
\[
 S_n=\sum_{u,v\in\mathbb Z/N}
 \omega^{-nv}
 \frac{W(Q,P,B;u+n)W(R,B,H;u+v)}
      {\overline W(R,Q,C;v)\overline W(C,P,H;u)}.       \tag{17}
\]
There is no division by the representation dimension in (16).
It is one matrix entry of the scalar composite, not its unnormalized
trace.

## 5. Evaluation with the complete normalization sum

Set
\[
 x=R/H,\qquad y=R/(\omega C),\qquad z=BC/(HQ),\qquad
 z_n=z\omega^{-n}.
                                                        \tag{18}
\]
These satisfy (10). Fix \(u\). The cyclic recurrence in (2) shows
that the \(v\)-sum in (17), before its other factors, is exactly
\[
 W(R,B,H;u)\, f(x\omega^u,y\mid z_n).                 \tag{19}
\]
Telescope (12) through \(u\) steps. Cancellation with the first
product in (19) gives
\[
 W(R,B,H;u) f(x\omega^u,y\mid z_n)
 =f(x,y\mid z_n)(B/H)^u
   \prod_{j=1}^{[u]}
       \frac{1-(Q/B)\omega^{n+j}}{1-(C/H)\omega^j}.
                                                        \tag{20}
\]
Here and below choose \(0\le u,n<N\); the periodic recurrences
retain any wrap in \(u+n\). To see the constants in (20), each
factor from (12), after canceling \(1-x\omega^{j+1}\), uses
\[
 \frac{x\omega^j-yz_n}{x\omega^j-y}
 =z_n\frac{1-(Q/B)\omega^{n+j+1}}
             {1-(C/H)\omega^{j+1}}.
\]
Multiplying (20) by \(W(Q,P,B;u+n)\) and dividing by
\(\overline W(C,P,H;u)\) cancels all remaining products except
\[
 W(Q,P,B;n) f(x,y\mid z_n)
                 \frac{1-C/H}{1-(C/H)\omega^u}.       \tag{21}
\]
The scalar powers cancel because
\((P/B)(B/H)/(P/H)=1\). Summing (21) over \(u\) yields
\[
 S_n=
 \frac{N(1-C/H)}{1-(C/H)^N}\,
 W(Q,P,B;n)f(x,y\mid z_n)
 =\frac{H^d}{\nu(P,C)^2}\,
 W(Q,P,B;n)f(x,y\mid z_n).                            \tag{22}
\]

There is one final finite telescope. From (11), the step from
\(n-1\) to \(n\), after multiplication by the corresponding step
of \(W(Q,P,B;n)\), has multiplier
\[
 \frac{P/B}{1-(Q/B)\omega^n}\,
 \frac{x-\omega yz\omega^{-n}}{1-z\omega^{-n}}
                  =\frac{PR}{BC-HQ\omega^n}.          \tag{23}
\]
Consequently
\[
 W(Q,P,B;n)f(x,y\mid z_n)
       =f(x,y\mid z)W(HQ,PR,BC;n).                   \tag{24}
\]
All these identities include \(n=0\) and \(n=N-1\).

For completeness, none of the telescoping denominators introduces
an extra genericity assumption on (13). In particular
\[
 \begin{gathered}
 1-x^N=B^N/H^N,\qquad 1-y^N=Q^N/C^N,\\
 1-z^N=-P^NR^N/(H^NQ^N),\qquad
 x^N-y^N=-P^NR^N/(H^NC^N),\\
 x^N-(yz)^N=-P^NR^N/(H^NQ^N),\qquad
 1-(C/H)^N=P^N/H^N .
 \end{gathered}                                         \tag{25}
\]
Every right side is nonzero. Multiplication of a parameter by a
power of \(\omega\) does not alter these checks. Thus all denominators
in (19)--(24) are nonzero on the stated regular domain.

Define
\[
 \kappa_*=
 \frac{\nu(P,Q)\nu(B,R)\nu(Q,R)}{\nu(P,C)},\qquad
 \rho=\kappa_* f\left(R/H,R/(\omega C)\mid BC/(HQ)\right).
                                                        \tag{26}
\]
Substituting (22),(24) into (16) proves the exact coefficient
\[
 \boxed{\displaystyle
 \mathscr R_{\alpha\beta}^{\gamma\delta}
 =\frac{\rho}{C^d}
   \omega^{\alpha\delta+\alpha^2/2}
   W(HQ,PR,BC;\gamma-\alpha)
   \delta_{\beta,\gamma+\delta}.}
                                                        \tag{27}
\]
The scalar (26) is precisely [K, (1.25)], with its three numerator
square roots and one denominator square root. Equation (27) is
the displayed (1.24), now derived from the complete literal bases.
There is no unresolved phase or multiplicative constant. Invertibility
also follows from (14), independently of the explicit inverse
calculation in [B].

## 6. The pentagon with indices and order retained

Take four objects \(p,q,r,s\), with all individual and contiguous
partial central sums nonzero. Use the same root and ordered-pair
normalization every time an object or a pair occurs. The coproduct
is coassociative: this follows directly on \(E,D\), hence on the
algebra they generate. Each of the five parenthesizations therefore
gives a complete basis of the same fourfold representation, by
iteration of (9).

Start with the tree \(((pq)r)s\), with multiplicity indices
\((\alpha,\beta,\gamma)\), and end with \(p(q(rs))\), with indices
\((u,v,w)\) from the outside inward. Reassociate first \(p,q,r\),
then \(p,qr,s\), then \(q,r,s\). Equations (14),(27) give its
coefficient as the left side below. Reassociating \(pq,r,s\) and
then \(p,q,rs\) gives the right side:
\[
 \begin{split}
 \sum_{a,b,c}
 &\mathscr R(p,q,r)_{\alpha\beta}^{ab}
  \mathscr R(p,qr,s)_{a\gamma}^{uc}
  \mathscr R(q,r,s)_{bc}^{vw}\\
 &=\sum_e
  \mathscr R(pq,r,s)_{\beta\gamma}^{ew}
  \mathscr R(p,q,rs)_{\alpha e}^{uv}.
 \end{split}                                             \tag{28}
\]
These are coefficients of the same actual initial columns in the
same complete final basis. Its inverse rows prove their equality.
With the lower multiplicity indices taken as matrix rows, (28) is
exactly
\[
 \mathscr R_{12}(p,q,r)\mathscr R_{13}(p,qr,s)
       \mathscr R_{23}(q,r,s)
 =\mathscr R_{23}(pq,r,s)\mathscr R_{12}(p,q,rs).       \tag{29}
\]
No projective scalar is left in this identity. Coassociativity alone
would not have fixed the entries of an unspecified multiplicity
basis; the finite evaluations (3)--(27) are what fix them here.

This proves the ordinary normalized recoupling tool. Charged
tetrahedra insert the specified Weyl operators and decoration
factors; their transport must retain those operators. Equation (29)
does not evaluate the nine-tetrahedron crossing array, choose a
conversion between the 1994 and 1995 normalizations, or identify
an original marked global source or a geometric saddle coefficient.
It asserts no even-level extension and no off-root quantum derivative.

## Direct sources

- [K] R. M. Kashaev, *Quantum Dilogarithm as a 6j-Symbol*,
  [hep-th/9411147v2](https://arxiv.org/pdf/hep-th/9411147v2).
  The complete thirteen-page text was read. Only its explicit
  representation, coproduct, finite-map and finite-product definitions
  are imported, not its recoupling or pentagon assertions.
  Local PDF: `research_archive/literal-charged-bubble-2026-11-17/kashaev1994.pdf`.
  SHA256 `dec5ba817a401b1ab88c6db1fbac6b8062c2cea05f19077097de247eca2642bb`.
- [B] [Literal charged tetrahedron inverse and bubble](research_literal_charged_tetrahedron_bubble.md).
  SHA256 `1dfe35f26137572235b1c3af66dcf410e0af758836baddaa8dd6d958c0f61d9b`.
  Its complete proof was read; the raw orthogonality used in (6)--(8)
  is also displayed explicitly here.
