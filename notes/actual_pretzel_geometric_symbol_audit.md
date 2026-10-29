# Literal pretzel coefficient phase, marked geometric saddles, and their action

**Subsequent global proof.** The
[full coherent period asymptotic](actual_pretzel_coherent_circle_and_period_asymptotic.md)
now establishes complete augmented-source survival by a finite inner
transformation, a global two-branch bound and real Gaussian estimates.
The local symbol audit below remains a separate verification; it is
not being promoted to a survival proof by itself.

29 October 2026. This independently checks the leading phase from the
EXACT finite factorial coefficients, its branch marks, all regular
stationary equations, and the nonzero full Hessian. The geometric
action has an explicit Lobachevsky formula. These are symbol and local
saddle statements only: no deformation of the original finite source,
nonzero thimble coefficient, or asymptotic dominance is proved here.

## 1. The actual finite term fixes the phase

Use the original complete-base polynomial
[with its source normalization](actual_pretzel_complete_base_casimir_polynomial.md):

\[
 \frac{\kappa z_N(w+w^{-1})}{N^2}
  =\sum_{0\leq r\leq v\leq M}t_{v,r}(w),\quad
 t_{v,r}=\frac{F_{2v}}{F_v^4}
          \frac{(Q^{-v};Q)_rQ^r}{F_r^3}
          (qw;Q)_r(q/w;Q)_r,
 \qquad M=\lfloor(N-1)/2\rfloor.                       \tag{1}
\]

Here F_a=(Q;Q)_a, q=exp(pi i/N), Q=q^2, and the original
kappa=q^((N-1)^2/2) is retained. On the interior physical index
triangle put X=Q^v, Y=Q^r. In a regular product-log chart the
leading exponent of the normalized term is N S/(2pi i), where

\[
\begin{split}
 S={}&-6\operatorname{Li}_2(1)-\operatorname{Li}_2(X^2)
       +4\operatorname{Li}_2(X)+\operatorname{Li}_2(X^{-1})
       -\operatorname{Li}_2(Y/X)\\
    &+\operatorname{Li}_2(w)+\operatorname{Li}_2(w^{-1})
       -\operatorname{Li}_2(wY)-\operatorname{Li}_2(Y/w)
       +3\operatorname{Li}_2(Y).                       \tag{2}
\end{split}
\]

For example log F_v has leading
N[Li2(1)-Li2(X)]/(2pi i). The first quotient in (1) gives
-3Li2(1)-Li2(X^2)+4Li2(X). The terminating Pochhammer gives
Li2(X^(-1))-Li2(Y/X), F_r^(-3) gives
-3Li2(1)+3Li2(Y), and the two remaining products give the four
w terms in (2). This is the product-log primitive continued from
the physical triangle, not a separately chosen favorable potential.
The factor Q^r is subleading in this scaling; the half-step q in the
last two products affects subleading amplitudes. The full original
z_N additionally contains kappa^(-1), whose unwrapped leading
contribution to S is +pi^2, a REAL constant per box. No imaginary
action or stationary equation is lost by recording it separately.

There is a check avoiding all primitive choices. The EXACT adjacent
finite term ratios are

\[
 \frac{t_{v+1,r}}{t_{v,r}}=
 \frac{(1-Q^{2v+1})(1-Q^{2v+2})}{(1-Q^{v+1})^4}
       \frac{1-Q^{-v-1}}{1-Q^{r-v-1}},
\]
\[
 \frac{t_{v,r+1}}{t_{v,r}}=
 Q\frac{(1-Q^{r-v})(1-qwQ^r)(1-qQ^r/w)}{(1-Q^{r+1})^3}. \tag{3}
\]

Their regular limits are exactly exp(S_x), exp(S_y), for
x=log X,y=log Y below. These identities retain the root phases
before taking a limit. They do not extend an interior assertion to
the terminating boundary r=v or to any collision divisor.

## 2. All regular sheets and the inner source marks

In logarithmic coordinates x,y,t=log w, differentiating (2) gives

\[
 e^{S_x}=\frac{(1+X)^2}{(X-1)(X-Y)},\qquad
 e^{S_y}=\frac{(1-Y/X)(1-wY)(1-Y/w)}{(1-Y)^3},\qquad
 e^{S_t}=\frac{wY-1}{w-Y}.                             \tag{4}
\]

A regular dilogarithm sheet change adds 2pi i times an INTEGER
linear form in x,y,t, plus a real multiple of 4pi^2. This follows
directly by continuing dLi2(z)=-Log(1-z)dLog z; every argument
in (2) is an integer monomial. Thus (4) and the Hessian are sheet
independent. A stationary PHASE also retains the corresponding
integer Fourier/Poisson marks; exponentiating alone forgets them.
When a sheet is changed those marks change by the same integer
linear form. The combined marked phase has unchanged imaginary
action. No choice of a different sheet may silently delete this
compensating source mark.

For an s-fold power in the actual positive winding m from the
finite enclosing residue, the explicit regular geometric branch
below uses PRINCIPAL dilogarithms. There one has

    S_x=0, S_y=2pi i, S_t=2i alpha, alpha=pi m/s.

Consequently its locally stationary marked phase is

\[
 \mathcal F=\sum_{i=1}^s
       [S(X_i,Y_i,w)-2\pi i\log Y_i]
                      -2\pi i m\log w.                 \tag{5}
\]

The inner y mark is compulsory on this sheet. It happens to change
only the REAL action at the geometric point because |Y_i|=1; that
does not justify dropping it before stationarity or continuation.
On the conjugate/reciprocal branch its y mark is -1 instead.
The exact finite winding weights, their double-pole multiplicities,
and the original common Cartan are still those of the source
formula. Equation (5) does not select a winding or a cycle for it.

## 3. Nondegenerate geometric solutions and the excluded factor

In the regular locus, the first two equations e^(S_x)=e^(S_y)=1
imply

\[
 X=\frac{Y-1}{Y+3},\qquad
 w+w^{-1}=6-\frac{16Y}{(1+Y)^2}.                       \tag{6}
\]

Factors Y=0, Y=1, X=0, X=1 and all zero denominators must be
excluded before using these rational equivalences. For the outer
condition put U=exp(2pi i m/s). Then Y=(Uw+1)/(w+U), and exact
substitution in the second equation of (6) yields

\[
 \frac{(w-1)^2}{w(w+U)^2}
       \{(1+U)^2(w^2+1)-2(U^2-6U+1)w\}=0.             \tag{7}
\]

For U!= -1, the factor w=1 gives Y=1, a collision rather than a
regular geometric saddle. It may not be retained as a nondegenerate
stationary branch. On the regular branch,

\[
 w+w^{-1}=2-\frac{16U}{(1+U)^2}
                 =2-4\sec^2\alpha.                    \tag{8}
\]

For 0<m<s/2, define

\[
 \eta=2\operatorname{arsinh}(\tan\alpha),\quad
 \beta=\arctan(\sec\alpha),\quad
 w=-e^\eta,\quad Y=e^{2i\beta},\quad
 X=\frac{i\sec\alpha}{2-i\sec\alpha}.                  \tag{9}
\]

These satisfy (4)--(8) and the marked derivatives in section 2.
All their dilogarithm arguments remain regular for fixed
alpha in (0,pi/2). This is the outside-|w| branch appropriate as
a candidate for the actual enclosing-circle representation. The
other regular solution for this U is obtained by w->1/w and
(X,Y)->(conjugate X,conjugate Y); its imaginary action is the
negative one. Neither statement proves a contour reaches either
point. For fixed odd s, the positive finite-source windings are
m=1,...,(s-1)/2 once N is sufficiently large, all within this range.

The principal integer marks can be verified without numerical
argument tracking. Put tau=sec(alpha)>1, A=atan(1/tau), B=atan(2/tau).
The four principal arguments in S_x are respectively
pi/2+A-2B, A-B, A, pi-A, with coefficients 2,-4,1,-1;
their sum is exactly zero. For S_y, Arg(1-Y/X)=pi-A and
Arg(1-Y)=-A. Both 1-wY and 1-Y/w lie in the upper half-plane,
the latter in its right half. Their product, using (4), has
principal argument pi-2A. Their argument sum is in (0,3pi/2),
so it equals pi-2A without a full turn. Thus S_y has argument
(pi-A)+(pi-2A)+3A=2pi. Finally S_t has imaginary part the
difference of these last two positive arguments, which is in
(-pi/2,pi). Equation (4) fixes it to 2alpha in (0,pi).
The real parts vanish by the same rational equations. These prove
the asserted 0,1,m/s marks on the entire connected branch.

At s=3,m=1, (9) is exactly

    w=-7-4sqrt3, X=(-1+i)/2, Y=(-3+4i)/5.

## 4. The FULL saddle Hessian is nonzero

Write the one-box Hessian in the logarithmic variables as

\[
 H_3=\begin{pmatrix}a&b&0\\b&d&e\\0&e&f\end{pmatrix},
\]

where

\[
 a=\frac{2X}{1+X}-\frac X{X-1}-\frac X{X-Y},
 \quad b=\frac Y{X-Y},
\]
\[
 d=-\frac Y{X-Y}-\frac{wY}{1-wY}-\frac Y{w-Y}
                                      +\frac{3Y}{1-Y},
\quad e=-\frac{wY}{1-wY}+\frac Y{w-Y},
\quad f=-1-\frac{wY}{1-wY}-\frac Y{w-Y}.                \tag{10}
\]

After the first relation in (6), its determinant is exactly

\[
 \det H_3=-\frac{Y(Y-1)(Y+3)^2(w^2-6w+1)}
                   {4(w-Y)(Y+1)^2(Yw-1)}.             \tag{11}
\]

On the second relation of (6), the inner two-by-two block K_2 has

\[
 \det K_2=-\frac{Y^2(Y+3)^2(w-1)^2}
                    {(w-Y)(Y+1)^3(Yw-1)}.             \tag{12}
\]

Both are NONZERO at (9). In particular checking only three
collective coordinates has not missed the antisymmetric modes
of the s actual copies. The full (2s+1)-variable Hessian of (5) has

\[
 \boxed{\det\operatorname{Hess}\mathcal F
              =s(\det K_2)^{s-1}\det H_3\ne0.}         \tag{13}
\]

This follows by its exact block Schur complement. Its effective
outer entry, before summing the s copies, is

    det H3/det K2=i cos(alpha)

on the expanding branch. It changes sign on the reciprocal branch.
This is a local saddle fact, not a global maximum or a statement
about the original integration-cycle intersection.

For the FULL power z_N^s there are also mixed regular inner
branches, which must not be suppressed. At a common negative
w<-1 the two inner solutions are the plus solution (9) and its
conjugate. Their outer characters are U and U^(-1), respectively,
and their inner y marks are +1 and -1. With k plus copies, put
n=2k-s. Since s is odd, n cannot vanish. On the principal product
chart the positive winding condition is

    n>2m, alpha=pi m/n

for the outside-|w| solutions. These are all regular stationary
possibilities in this chart for a positive source winding: the
inner quadratic has only its reciprocal Y pair; the outer product
is U^n=1, and the regular elimination (7) then fixes negative real
w. The zero-winding possibility U=1 is not part of the exact source
sum, whose windings start at 1. In particular it need not be treated
as a selected saddle of that source. The reciprocal-|w| solutions
have a majority of conjugate copies and negative action.

The exact mixed Hessian has outer Schur entry n i cos(alpha) and

\[
 \det\operatorname{Hess}\mathcal F
       =(\det K_2)^k(\overline{\det K_2})^{s-k}
                            n i\cos\alpha\ne0.         \tag{13a}
\]

This retains every one of the 2s independent inner variables. The
binomial number of arrangements is finite for a fixed source width;
it is not an additional exponential multiplicity as N grows.

## 5. The real imaginary-action formula

Define Lambda(theta)=-integral_0^theta log|2sin t| dt. For (9),
the fully marked phase has

\[
 \boxed{\operatorname{Im}\mathcal F
 =8s\{\Lambda(\tfrac\pi4+\tfrac\alpha2)
           +\Lambda(\tfrac\pi4-\tfrac\alpha2)\}.}       \tag{14}
\]

Here is a derivation that does not assume a known antiprism volume
or the survival of this saddle. Set
V(alpha)=Im S(X,Y,w)-2alpha eta. Along (9), y=2i beta and
t=eta+i pi. The derivatives in section 2 give

    d(Im S)/dalpha=2alpha eta',
    V'=-2eta=-4arsinh(tan alpha).

The right side of (14), divided by s, has the SAME derivative, since

    sin(pi/4+alpha/2)/sin(pi/4-alpha/2)
       =sec alpha+tan alpha,

whose logarithm is arsinh(tan alpha). The common integration
constant is zero at alpha->pi/2. To check the latter directly,
X,Y tend to -1 and all bounded dilogarithms have vanishing imaginary
limits. The only unbounded pair is Li2(w)-Li2(wY). The elementary
inversion identity, proved by differentiation and evaluation at -1,

    Li2(z)+Li2(1/z)=-pi^2/6-(1/2)Log(-z)^2,

shows that its imaginary part is 2beta eta+o(1).
As beta-alpha=O(pi/2-alpha),
2(beta-alpha)eta tends to zero. Hence V tends to zero, as does
the Lobachevsky expression. This proves (14).

For s=3,m=1, triplication of Lambda gives the exact value 4v8,
where v8=8Lambda(pi/4). The same formula for other s is the
formal four-antiprism action with the stated winding alpha. This
identification of a REAL formula does not assume that the original
augmented link's invariant has this growth, or identify a filled
knot from that action. The original-cycle/boundary and possible
multi-winding cancellation questions remain outside this theorem.

For completeness, the mixed branch with effective n in (13a) has
the SAME formula with s replaced by n and alpha=pi m/n. This
follows since the two inner actions are complex conjugates at
negative real w; their imaginary parts subtract. All such mixed
outside actions are strictly below the all-plus n=s action at the
same m. Indeed V(alpha)>0 and V'(alpha)<0 for 0<alpha<pi/2, so

\[
 \frac d{dn}\{nV(\pi m/n)\}=V(\alpha)-\alpha V'(\alpha)>0.
                                                               \tag{15}
\]

The all-plus action in turn strictly decreases with the positive
winding m. Hence m=1 and n=s give the UNIQUE largest regular
imaginary action among these actual positive-winding stationary
systems, apart from identical labeling of equal copies. This is
an interior critical-value gap, NOT a contour-height or boundary
gap. In particular the equal-height diagonal collision boundary
in the independent boundary analysis is not ruled out here.

The [audit](../experiments/audit_actual_pretzel_geometric_symbol.py)
checks the literal finite ratios, exact elimination and Hessian
identities, every positive winding at several odd widths, both
reciprocal branches, the actual integer inner marks, and the full
Lobachevsky action. It does not numerically estimate a selected
cycle coefficient.
