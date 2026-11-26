# The factorial optimizing sum lies above one half

Research deduction, 6 November 2026. The lower summed-angle branch in
the first-four/next-three factorial problem is impossible. This proof
uses the original marginal derivatives and already-proved optimizing
coordinate restrictions at the unchanged actual heights. Only
elementary inequalities and rational polynomial identities are used.

## 1. Scope and derivative signs

Use the original phase \(\mathcal F(e,s,z,b)\), outgoing affine
subtraction and factorial path from the
[height-envelope theorem](research_mixed_selected_boundary_height_envelope.md).
The first selected vertex is type four, its next vertex is ordinary
type three, and the word has length at least three. Put
\(k=\Im z,\ x=\Re z,\ y=\Re s\). At every factorial maximizer,
\[
 \begin{gathered}
 .3<\Re e<.4,\quad .2<y\le.5,\quad .22\le x<3/8,
                    \quad .22\le\Re b\le.45,\\
 -.051<\Im e<-.019,\quad -.065<\Im s,\Im b<.068,
                    \quad -.07<k\le.014.
 \end{gathered}
\tag{1}
\]
These are proved optimizing bounds, not independently substituted
reference data. Write \(D_s=\Re\mathcal F_s,D_z=\Re\mathcal F_z\).
Since \(z\) is below its original upper endpoint, \(D_z\le0\),
including at \(x=.22\). If \(x+y\le.5\), then
\(.2<y\le.28<.5\), so \(s\) is interior and \(D_s=0\).
The outgoing affine subtraction affects neither derivative.

**Theorem.** Every such factorial maximizer satisfies
\[
                              \Re(s+z)>\frac12.
\tag{2}
\]

## 2. Excluding \(x\le.23\) on the lower-sum branch

Suppose \(x+y\le.5\) and \(x\le23/100\). Put
\(E=e^{-2\pi ie},S=e^{-2\pi is},Z=e^{-2\pi iz},R=|Z|\).
The original chirp gives
\[
 e^{2D_z}=\frac{|1-EZ|^2\,|S^{-1}-Z|^2}{|1-Z|^6}.
\tag{3}
\]
The restrictions imply
\[
 \begin{gathered}
 |E|>18/25,\quad |S|^{-1}>13/20,\quad 3/5<R<11/10,\\
 \cos(2\pi\Re(e+z))<-2/3,\quad
 \cos(2\pi\Re(s+z))<-87/100,\quad
 \cos(2\pi x)>1/8.
 \end{gathered}
\tag{4}
\]
Indeed \(\Re(e+z)\in(.52,.63)\) and
\(\Re(s+z)\in(.42,.5]\). Explicit witnesses are
\[
 \begin{split}
 \cos(.26\pi)&=\sin(.24\pi)>
             \tfrac34-\tfrac{(3/4)^3}{6}=\tfrac{87}{128}>\tfrac23,\\
 \cos(.16\pi)&>1-\tfrac12(88/175)^2
                 =\tfrac{87}{100}+\tfrac{437}{122500},\\
 \sin(.04\pi)&>\tfrac{157}{1250}
                   -\tfrac{(157/1250)^3}{6}>\tfrac18.
 \end{split}
\tag{5}
\]
Here \(157/50<\pi<22/7\). The elementary bound
\[
 e^t\le1+t+\frac{t^2}{2(1-t/3)}\qquad(0<t<3)
\tag{6}
\]
at \(t=13/40,3/7,11/25,11/125\) gives respectively
\(e^{.102\pi}<25/18,\ e^{.136\pi}<20/13,\
e^{.14\pi}<5/3,\ e^{.028\pi}<11/10\).
It proves all radius bounds in (4).

Both numerator moduli increase with their positive radius under
these negative cosine bounds. Hence
\[
 e^{2D_z}>
 \frac{(1+324R^2/625+24R/25)
                (R^2+169/400+1131R/1000)}
      {(1+R^2-R/4)^3}>1.
\tag{7}
\]
To prove the last inequality, let \(F(R)\) be numerator minus
denominator. For \(u=R-3/5\), the exact identity is
\[
 \begin{split}
 F(3/5+u)={}&\frac{502380579}{625000000}
 +\frac{280946079}{125000000}u
 -\frac{36512207}{25000000}u^2
 -\frac{24819523}{5000000}u^3\\
 &-\frac{58191}{10000}u^4-\frac{57}{20}u^5-u^6.
 \end{split}
\tag{8}
\]
It is strictly concave for \(u\ge0\). Its values at \(R=3/5,11/10\)
are \(502380579/625000000\) and \(2368009237/5000000000\),
both positive. Thus (7) contradicts \(D_z\le0\).

## 3. Excluding \(x\ge.23\) on the lower-sum branch

Suppose now \(x\ge23/100\) and \(x+y\le.5\). Necessarily \(x<.3\).
Increase \(y\), with \(x\) and all other data fixed, to
\(y_0=.5-x\in(.2,.27]\). The proved common horizontal concavity
makes \(D_s\) decrease during this change. Then move along
\(x+y=.5\), increasing \(y\) to \(.27\) and decreasing \(x\)
to \(.23\), keeping every height and \(b\) fixed. Along this line,
\[
 \frac{dD_s}{dy}
       =\pi\Re\{\cot\pi(s+b)-2\cot\pi s\}<0.
\tag{9}
\]
For the inequality, \(y\in[.2,.27]\) gives
\(\Re\cot\pi(s+b)\le\cot(.42\pi)<1/3\), and
\(\Re\cot\pi s>3/4\). The latter follows because its numerator
is at least \(\sin(.4\pi)>19/20\), while its denominator is less
than \(11/10+13/100=123/100\). Use
\(\cosh(.136\pi)<\cosh(11/25)<11/10\),
\(\sin(.04\pi)<13/100\), and
\(\cos(.1\pi)>1-(11/35)^2/2>19/20\).
The hyperbolic-cosine estimate follows from
\(1+t^2/2+t^4/[24(1-t^2/30)]\) at \(t=11/25\).
For the former bound, use
\(\cot(.42\pi)=\tan(.08\pi)
 <(13/50)/(1-(13/50)^2/2)<1/3\).
Thus (9) is in fact less than \(-7\pi/6\).

It suffices to bound \(D_s\) at \(y=.27,x=.23\).
Set \(r=|S|,\ q=|Z|^{-1},\ t=|B|\). Since \(SZ\) is negative
real, the exact chirped derivative there is
\[
                 e^{2D_s}=(q+r)^2\frac{|1-SB|^2}{|1-S|^4}.
\tag{10}
\]
For \(\Re b\in[.22,.45]\), the real sum \(s+b\) lies in
\([.49,.72]\); its cosine is largest at \(.72\).
Thus \(|1-SB|^2\) is smallest at \(\Re b=.45\).
At that endpoint its cosine is negative, so it increases with \(t\).
The height bounds imply
\[
       13/20<r<31/20,\qquad q>91/100,\qquad t>33/50.
\tag{11}
\]
For the last two inequalities apply (6) at
\(41/100>.13\pi\) and \(11/125>.028\pi\); its bounds are less
than \(50/33\) and \(100/91\), respectively.
The interval for \(r\) follows from the same estimates and
\(e^{.136\pi}<20/13<31/20\). Also
\[
 -2\cos(1.44\pi)=2\sin(.06\pi)>37/100,\qquad
 -2\cos(.54\pi)=2\sin(.04\pi)<13/50.
\tag{12}
\]
The first uses the cubic sine lower bound at \(3/16<.06\pi\);
the second uses \(\sin t<t\). Consequently
\[
 e^{2D_s}>
 \frac{(r+91/100)^2
        (1+(33/50)^2r^2+(37/100)(33/50)r)}
      {(1+r^2+13r/50)^2}>1.
\tag{13}
\]
The difference polynomial in (13) is
\[
 P(r)=-\frac{1411}{2500}r^4+\frac{8078}{15625}r^3
       -\frac{6560891}{25000000}r^2
       +\frac{75111101}{50000000}r-\frac{1719}{10000}.
\tag{14}
\]
It is strictly concave on \([13/20,31/20]\):
\(P'''\) decreases and \(P'''(13/20)=-178209/31250<0\),
while \(P''(13/20)=-17126381/12500000<0\).
Its endpoint values are \(1837238139/2500000000\) and
\(241919703/1250000000\), both positive. This proves (13).
Reversing the two derivative-decreasing transports yields \(D_s>0\)
at the hypothetical maximum. But there \(s\) is strictly interior,
requiring \(D_s=0\). This proves the theorem.

## 4. Consequences and limits

Together with the [proved upper sum bound](research_mixed_factorial_next_three_sum_bound.md),
the theorem gives
\[
        \frac12<\Re(s+z)<\frac{41}{50},\qquad
                   b_s=-\Re\cot\pi(s+z)>0
\tag{15}
\]
on the entire original next-three factorial optimizing path.
In particular \(SZ\) has positive imaginary part. Only the positive
square-root sign for \(SZ\) can survive the maximizing constraints
in the [interior reconstruction](research_mixed_interior_optimizer_reconstruction.md).
This removes the other summed-angle branch; it does not assert that
the maximum is interior.

No imaginary height or outgoing tangent was changed. This is a sign
and branch restriction for the ordinary Schur stiffness, not the
required quantitative bound for it. The six-pi determinant, integrated
selected budget and all unhandled finite-source currents remain
separate obligations.

## 5. The other ordinary sum and its private stiffness

The same factorial maximizers also satisfy
\[
                              \Re(s+b)>\frac12.
\tag{16}
\]
This follows from a direct lower bound on the original \(s\)
marginal. Suppose instead that \(\Re(s+b)\le.5\).
Then \(.2<y\le.28\), so \(s\) is strictly interior and
\(D_s=0\). The literal sine form of that marginal is
\[
 e^{D_s}=e^{\pi(\Im b-k)}
      \frac{|\sin\pi(s+z)|\,|\sin\pi(s+b)|}
           {|\sin\pi s|^2}.
\tag{17}
\]
In particular the signed height term of the original chirp remains.

The hypothetical coordinate ranges give
\(\Re(s+z)\in(.42,.655)\) and
\(\Re(s+b)\in(.42,.5]\). Hence
\[
 |\sin\pi(s+z)|>22/25,
 \qquad |\sin\pi(s+b)|>24/25,
 \qquad |\sin\pi s|^2<13/20.
\tag{18}
\]
Here \(|\sin\pi(x+ih)|^2=\sin^2\pi x+\sinh^2\pi h\).
For the first bound the smallest allowed real sine is bounded by
\(\sin(.345\pi)>\sin(27/25)\), and the seventh-degree
Taylor lower bound gives
\[
 \frac{27}{25}-\frac{(27/25)^3}{6}
 +\frac{(27/25)^5}{120}-\frac{(27/25)^7}{5040}
       =\frac{22}{25}+\frac{6673092283}{3417968750000}.
\tag{19}
\]
For the second bound,
\(\sin(.42\pi)=\cos(.08\pi)>1-(13/50)^2/2>24/25\).
For the denominator, \(\sin^2(.28\pi)
=(1+\sin(.06\pi))/2<3/5\). Also
\(|\pi\Im s|<.068\pi<3/14\), and the positive-series
upper bound for hyperbolic sine gives
\[
 \sinh(3/14)
 \le \frac3{14}
    +\frac{(3/14)^3}{6(1-(3/14)^2/20)}
       =\frac{11}{50}-\frac{398}{97775}
       <\frac{11}{50}.
\tag{20}
\]
Its square is less than \(1/20\), proving the last bound in (18).

Finally \(\pi(\Im b-k)>-.079\pi>-1/4\), and (6) gives
\(e^{1/4}\le113/88<9/7\). Inserting these estimates in
(17) yields
\[
                  e^{D_s}>
 \frac{(7/9)(22/25)(24/25)}{13/20}
                         =\frac{4928}{4875}>1.
\tag{21}
\]
This contradicts \(D_s=0\) and proves (16).

The new sign supplies an explicit positive part of the ordinary
Schur stiffness. Put
\(a_s=\Re\cot\pi s\ge0\),
\(a_b=\Re\cot\pi b>0\), and
\(j=-\Re\cot\pi(s+b)>0\); the upper sum is at most
\(.95<1\). The unchirped pair \(V(s,b)\) has real negative
Hessian, divided by \(\pi\),
\[
             \begin{pmatrix}a_s+j&j\\j&a_b+j\end{pmatrix}.
\tag{22}
\]
Eliminating a free outgoing coordinate therefore contributes exactly
\[
 \delta_{sb}=a_s+j-\frac{j^2}{a_b+j}
            =a_s+\frac{ja_b}{a_b+j}>a_s.
\tag{23}
\]
For the full original next-three problem, with
\(b_s=-\Re\cot\pi(s+z)>0\) from (15), the ordinary pivot
in the active-face curvature criterion is
\[
 T=\begin{cases}
 2a_s+b_s+\dfrac{ja_b}{a_b+j},&b\text{ free},\\
 2a_s+b_s+j,&b\text{ on an original endpoint}.
 \end{cases}
 \qquad T>2a_s+b_s\ge b_s.
\tag{24}
\]
The last comparison allows \(a_s=0\) on the original face
\(s_R=.5\); the conclusion \(T>b_s\) remains strict.
No independence of the outgoing phase from its original tangent
is used. This positive stiffness contribution has not yet been
shown to pay the full cancellation threshold for the six-pi bound.

## 6. Actual positive-height motion, including outgoing faces

The preceding signs and the two original face exclusions now discharge
the extra assumptions of Section 10 of the
[height-envelope proof](research_mixed_selected_boundary_height_envelope.md)
for the next-three factorial maximum. This consequence concerns only
its positive-height segment, with the original reference heights and
outgoing tangent fixed.

Let \(x(k)=(e_R(k),s_R(k),z_R(k),b_R(k))\) denote that maximum
for \(0\le k\le H\le7/500\). The
[lower](research_mixed_factorial_lower_face_exclusion.md) and
[upper](research_mixed_factorial_upper_face_exclusion.md) face theorems
make \(e_R,s_R,z_R\) interior. The original outgoing coordinate
may be free or at an endpoint. Define \(E_0,b_e,b_s,q_e,q_s,q_z\)
as in the [active-face theorem](research_mixed_active_face_curvature_budget.md),
and choose \(T\) by (24) according to this actual outgoing status.
The free real Hessian is positive definite, so
\[
 D_0=a_0-b_e^2/E_0-b_s^2/T>0,\qquad T>b_s>0.
\tag{25}
\]
The maximum is Lipschitz. At almost every height the active-face
response theorem gives
\[
 \begin{split}
 z_R'&=Q/D_0,\qquad
 Q=q_z-b_eq_e/E_0-b_sq_s/T,\\
 e_R'&=(q_e-b_ez_R')/E_0,\qquad
 s_R'=(q_s-b_sz_R')/T.
 \end{split}
\tag{26}
\]
If the outgoing coordinate is active, its derivative is zero at every
height where it is differentiable; eliminating it then gives exactly
the second case of (24). No strict complementarity is needed.

Write \(v_e=\Im\cot\pi(e+z)\) and
\(v_z=\Im\cot\pi z\). On the entire positive segment the proved
summed-angle and height bounds give
\(0<v_e<1\), \(v_z\le0\), and \(q_s<0\). Consequently
\[
 Q=3v_z+q_s(1-b_s/T)-v_e
                      -\frac{b_e(1-v_e)}{E_0}<0.
\tag{27}
\]
It follows that
\[
 z_R'<0,\qquad e_R'>0,\qquad
 (s_R+z_R)'=\frac{q_s+(T-b_s)z_R'}{T}<0
 \quad\hbox{almost everywhere}.
\tag{28}
\]
Absolute continuity upgrades these almost-everywhere signs to strict
monotonicity on every nontrivial positive-height subinterval. In
particular \(z_R(k)\le z_R(0)\) and
\(s_R(k)+z_R(k)\le s_R(0)+z_R(0)\), with strict inequalities
when \(k>0\), while \(e_R(k)>e_R(0)\).

This is a proved motion of the actual factorial maximizing family,
including arbitrary changes of its outgoing active status. It does
not determine the sign of \(s_R'\) alone, extend the conclusion to
the negative reset, or establish the remaining curvature or finite
source bound. It does not concern the forced phase, whose derivative
column differs.

**Corollary.** Throughout this positive-height next-three factorial
segment,
\[
                         \Re z<31/100.
\tag{29}
\]
It suffices first to check height zero. At the proposed real cut
\(z_R=31/100\), the already proved private range gives
\(.61<\Re(e+z)<.71\), so
\(\cos(2\pi\Re(e+z))>-39/50\). The actual fixed heights give
\(|E|<89/100\) and \(|S|^{-1}<151/100\), where
\(E=e^{-2\pi ie}\) and \(S=e^{-2\pi is}\). For explicit
elementary witnesses, with \(c_4(t)=1-t^2/2+t^4/24\),
\[
\begin{split}
 \frac{39}{50}-c_4(69/100)&=\frac{6884293}{800000000}>0,\\
 1+\frac{119}{1000}+\frac{(119/1000)^2}{2}
       -\frac{100}{89}&=\frac{442329}{178000000}>0,\\
 \frac{151}{100}-\left\{1+\frac{409}{1000}
       +\frac{(409/1000)^2}{2(1-409/3000)}\right\}
       &=\frac{21539}{5182000}>0.
\end{split}
\tag{30}
\]
Indeed \(.22\pi>.69\), \(.038\pi>.119\), and
\(.13\pi<.409\). The cosine Taylor bound and the positive
exponential series, with its tail bounded geometrically after the
quadratic term, give the stated inequalities. Also
\(\sin(.12\pi)>\sin(3/8)>3/8-(3/8)^3/6>9/25\);
the last difference is \(159/25600\).

At height zero, \(|Z|=1\). The literal derivative in (3) therefore
satisfies, at this cut,
\[
 e^{2D_z}
 =\frac{|1-EZ|^2\,|S^{-1}-Z|^2}{|1-Z|^6}
 <\frac{\{1+(89/100)^2+(39/25)(89/100)\}(251/100)^2}
          {(68/25)^3}<1.
\tag{31}
\]
The numerator is exactly \(400749361/20000000\), and the
denominator minus this numerator is \(1723599/20000000>0\).
For fixed other coordinates, the original real \(z\) derivative
strictly decreases from this cut to any larger allowed coordinate:
the two summed real parts \(\Re(e+z),\Re(s+z)\) lie in
\((1/2,1)\), while \(\Re z<1/2\), so
\(\Re\mathcal F_{zz}<0\). Thus a factorial maximum at height
zero cannot have \(z_R\ge31/100\). The strict decrease proved
in (28) propagates (29) through every positive height in the
stated segment. No conclusion about this cut on the negative
reset, or about the remaining six-pi estimate, is included.

