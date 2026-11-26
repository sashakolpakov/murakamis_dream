# Horizontal action decay on the whole upper incoming unit semicircle

Private written proof, 10 November 2026. The multiplier of the
original type-four conditional critical action has modulus strictly
less than one on the entire upper incoming unit semicircle, excluding
the endpoint \(X=1\). No sign of its imaginary part is assumed.
The proof handles the lower-half-plane multiplier directly.

This is an action theorem. It does not replace the complete finite
conditional polynomial by its critical exponential.

## 1. Original branch, multiplier and statement

Use the exact finite source
\[
 C_{1,N}(X,Y)=\sum_{j=0}^{N-1}
 \frac{X^{-j}(q_NX;q_N)_j(q_NY;q_N)_j}{(q_N;q_N)_j^3},
 \qquad q_N=e^{-2\pi i/N},
 \tag{1}
\]
and the original phase
\[
 Q(t;a,y)=g(a+t)+g(y+t)-3g(t)-g(a)-g(y)+2\pi iat .
 \tag{2}
\]
All primitive constants, logarithmic branches, the incoming carrier
and finite summation endpoints remain unchanged.
On
\[
 \mathcal U=\{X:|X|=1,\ \Im X>0\}\cup\{-1\},\qquad
 \mathcal Y=\{Y:\Im Y<0,\ \Re Y<1\},
 \tag{3}
\]
the [unit incoming branch theorem](research_mixed_four_conditional_unit_incoming_branch.md)
gives the unique simple upper root \(v\) of
\[
                 v(v-X)(v-Y)=X(v-1)^3 .
 \tag{4}
\]
It excludes \(v=0,1,X\). With the original continuous arguments,
\[
 a=1-\frac{\Log X}{2\pi i}\in[1/2,1),\qquad
 y=-\frac{\Log Y}{2\pi i},\qquad
 t=\frac{\Log v}{2\pi i},\qquad
 0<\Re t<1-a,\qquad Q_t=0 .
 \tag{5}
\]
Define
\[
          \Theta(a,y)=Q(t(a,y);a,y),\qquad
                    \omega=\frac{v-X}{1-X}.
 \tag{6}
\]

**Theorem 1.** Throughout (3),
\[
                         0<|\omega|<1 .
 \tag{7}
\]
Consequently the same calibrated critical action satisfies
\[
                    \partial_a\Re\Theta=\log|\omega|<0
                         \qquad(a\ \hbox{real}).
 \tag{8}
\]
On every compact parameter subset of (3), the right side is
bounded above by a strictly negative constant. No assertion about
\(\Im\omega\), a principal logarithm of \(\omega\), or vertical
action monotonicity is made.

## 2. The exact unit-multiplier boundary identity

Suppose, for contradiction, that \(|\omega|=1\).
Write
\[
 X=c+iB,\qquad A=1-c,\qquad
 \omega=k+is,\qquad d=2(1-k),\qquad P=|v|^2 .
 \tag{9}
\]
First assume \(\Im X=B>0\), so \(A>0\), and
\[
                         B^2=A(2-A).
 \tag{10}
\]
The value \(\omega=1\) would give \(v=1\), already excluded.
Thus \(d>0\). The exact identity \(v=X+(1-X)\omega\) gives
\[
\begin{split}
 P&=1+Ad+2Bs,\\
 \Re v&=1-\frac{Ad}{2}+Bs,\qquad
 \Im v=\frac{Bd}{2}+As,\\
 P-\Re v&=\frac{3Ad}{2}+Bs .
\end{split}
\tag{11}
\]

Solving (4) for \(Y\) and using
\((\omega-1)^2/\omega=-d\) yields the exact formula
\[
             Y=v+dX(1-X)(1-v^{-1}).
 \tag{12}
\]
Put
\[
 C=\Re[X(1-X)]=A(1+2c),\qquad
 D=\Im[X(1-X)]=B(1-2c).
\]
Its imaginary part is
\[
 P\Im Y=(\Im v)(P+dC)+dD(P-\Re v).
 \tag{13}
\]
Substitute (10)--(11), and use the unit-circle identity
\(s^2=d-d^2/4\). Expanding and collecting terms gives
\[
 \boxed{\;
 P\Im Y=
 B d\left(\frac12+2A\right)+2A^2B d^2
                   +As(1+4B^2d).
 \;}
 \tag{14}
\]
For example, the intermediate simplification
\(P+dC=1+2Bs+2B^2d\) fixes the signs of the last terms.
Formula (14) is purely algebraic and retains the original
carrier in (4).

If \(s\ge0\), every term in (14) is nonnegative and its first
term is strictly positive. Therefore \(\Im Y>0\), contrary
to (3). This includes \(\omega=-1\), for which \(s=0,d=4\).

## 3. The lower-half-plane multiplier

It remains to consider \(s<0\). Write, with \(\tau,\ell>0\),
\[
 X=\frac{1+i\tau}{1-i\tau},\qquad
 \omega=\frac{1-i\ell}{1+i\ell}.
 \tag{15}
\]
Every such pair in the open upper and lower semicircles has
these unique parameters. In particular
\[
 A=\frac{2\tau^2}{1+\tau^2},\qquad
 B=\frac{2\tau}{1+\tau^2},\qquad
 \frac BA=\frac1\tau,\qquad
 d=\frac{4\ell^2}{1+\ell^2},\qquad
 s=-\frac{2\ell}{1+\ell^2}.
 \tag{16}
\]
Direct substitution in \(v=X+(1-X)\omega\) gives
\[
 v=\frac{1-3\tau\ell-i(\tau-\ell)}
          {1+\tau\ell-i(\tau-\ell)},\qquad
 \Im v=
 \frac{4\tau\ell(\ell-\tau)}
      {(1+\tau^2)(1+\ell^2)} .
 \tag{17}
\]
The root is in the upper half-plane, so
\[
                             \ell>\tau .
 \tag{18}
\]
No incoming-ray restriction is needed for this implication.

Substituting (16) in (14) and factoring gives
\[
 P\Im Y=-\frac{2A\ell}{1+\ell^2}\,\mathcal L ,
 \qquad
 \mathcal L=1-\frac{\ell}{\tau}
       -\frac{4B\ell}{1+\ell^2}\,\mathcal R ,
 \tag{19}
\]
where
\[
\begin{split}
 \mathcal R
 &=1-4B\ell+(1+4A)\ell^2\\
 &=(1-2B\ell)^2+(1-2A)^2\ell^2\ge0 .
\end{split}
\tag{20}
\]
The second identity uses (10).
Since (18) makes the first two terms in \(\mathcal L\)
strictly negative, (19)--(20) imply \(\mathcal L<0\).
Its prefactor in (19) is negative. Hence again \(\Im Y>0\),
contrary to (3).

For the remaining incoming endpoint \(X=-1\), one has
\(A=2,B=0\) and \(v=-1+2\omega\).
The upper-root condition implies \(s>0\).
The same algebraic identity (14) then reduces to
\(P\Im Y=2s>0\), giving the same contradiction.
This completes the exclusion of \(|\omega|=1\) everywhere
on (3).

## 4. Continuation, the original action and exact limitations

The parameter set (3) is connected, and the root in (5) is
continuous and locally holomorphic there. The multiplier is
nonzero because \(v\ne X\), and its denominator is nonzero
because \(X\ne1\). Along every compact parameter path it remains
finite. At the original anchor \(X=-1,Y=-i,v=i\),
\[
                   \omega=\frac{1+i}{2},\qquad
                          |\omega|^2=\frac12<1 .
 \tag{21}
\]
The unit-boundary exclusion therefore proves (7) by continuation.
It uses only \(\Im Y<0\) in the boundary calculation; the
additional condition \(\Re Y<1\) is retained to license the
original root count and logarithmic phase throughout the domain.
In particular actual outputs with \(|Y|\le1,\Im Y<0\) are
included without an additional radius restriction.

Stationarity in the original, unsquared logarithmic phase gives
\[
 \Theta_a=g'(a+t)-g'(a)+2\pi it,\qquad
                   e^{\Theta_a}=\frac{v-X}{1-X}=\omega .
 \tag{22}
\]
Taking absolute values in this exact identity gives (8).
There is no need to identify \(\Theta_a\) with a principal
logarithm after its multiplier moves into a different half-plane.
The original zero lift and additive primitive constant remain
those fixed by (5).

Continuity and (7) give a uniform negative upper bound for
\(\log|\omega|\) on every compact parameter subset. Thus for
fixed \(y\) and \(1/2\le a_1<a_2<1\),
\[
                     \Re\Theta(a_2,y)<\Re\Theta(a_1,y).
 \tag{23}
\]
The strictness is uniform on compact families staying away
from \(X=1\) and from the outgoing-domain boundary.

No uniform margin at the excluded periodic endpoint is asserted.
Equations (7)--(23) neither bound the physical end rows of (1)
nor pay its aliases, unweighted connectors, multiplying cap,
or Fourier weight. A complete finite-source upper comparison
on any newly reached real interval must retain those separate
obligations. No whole-period, whole-word or knot conclusion
is inferred.

## Direct source versions

| Direct source | SHA-256 |
|---|---|
| research_mixed_four_conditional_unit_incoming_branch.md | b6c8fdaffd436ec82670ec864629d93d36e7c7a8ae7e81033b684e3f86e92e43 |
| research_mixed_four_conditional_positive_incoming_action.md | e8608019efbd73b2c05e6ede084b4781182259dc0e32be12b4610c66f352d371 |
| research_mixed_conditional_torus_composition.md | 8a25a25a95bf11767c4f305317a6fab9a9c17724ae0e24a36014b5fd8ec4f693 |

The entire proof and its directly used source implications were read
in full, and all three source bindings were checked. Independent
proof/direct-source review is required before adoption.
No mathematical numerical evaluation, saved-value
arithmetic, test, import, compilation or frozen-source edit is used.
