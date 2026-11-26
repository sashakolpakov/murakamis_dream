# A filled cover cannot make its short meridian geometrically long

25 November 2026. Research proof.

The proposed cover shortcut has a necessary filling-compatibility condition.
It prevents using an unbranched cover to turn a fixed short filling into
a long one while retaining multiplication of the completed hyperbolic
volume by the covering degree. This is a check on that route, not a
quantum descent statement or a restriction of the finite-exception target.

Let \(X\) be a complete hyperbolic drilled exterior, and let \(Y=X(s)\)
denote some prescribed fillings along primitive slopes \(s_i\). Suppose
\(p:Y'\to Y\) is a finite unbranched cover of degree \(D\).
Drill every preimage of each filling core to obtain \(X'\to X\).
Equip \(X'\) with the pullback of the complete drilled metric on \(X\).
For a horotorus \(T_i\), let \(T'_{ij}\to T_i\) have degree \(d_{ij}\),
and define normalized slope length by
\[
 \mathcal L_T(s)=\frac{\operatorname{length}_T(s)}
                         {\sqrt{\operatorname{area}(T)}}.
\]
Changing the size of the horotorus does not change this ratio.

The primitive filling meridian \(s'_{ij}\) upstairs maps to
\(\pm s_i\), rather than to a higher multiple. Indeed each component
of the inverse image of the filled solid torus is an unbranched solid-
torus cover. A meridian disk downstairs lifts to disks mapped
homeomorphically to it, since the disk is simply connected. Their
boundaries are the primitive upstairs meridians. Equivalently, the
boundary subgroup contains \(s_i\), the kernel of the map from the
boundary fundamental group to that of the solid torus.

The lifted flat metric gives
\[
 \operatorname{area}(T'_{ij})=d_{ij}\operatorname{area}(T_i),
 \qquad
 \operatorname{length}(s'_{ij})=\operatorname{length}(s_i),
 \qquad
 \boxed{\mathcal L(s'_{ij})=\mathcal L(s_i)/\sqrt{d_{ij}}.}
\]
In particular the normalized length does not increase. If all the
preimage filling cores are retained, \(\sum_jd_{ij}=D\) for each \(i\).
For the simultaneous parameter
\(\mathcal L_{\mathrm{tot}}^{-2}=\sum_i\mathcal L(s_i)^{-2}\), this gives
\[
                 \mathcal L_{\mathrm{tot}}(X')
                      =\mathcal L_{\mathrm{tot}}(X)/\sqrt D.
\]

A cover of the unfilled exterior can instead have primitive lifted
slope mapping to \(ks_i\), \(k>1\). Its normalized length is
\(k\mathcal L(s_i)/\sqrt{d_{ij}}\), but that filling map cannot extend
unbranched across the core: its meridian has degree \(k\). A branched
completion does not supply the unbranched completed-volume law used by
the proposed descent. This distinction does not rule out a different
drilling construction or a separately proved branched quantum identity.

The [earlier cover analysis](regge_period_covers_and_a_curves.md) gives
peripheral isogenies, the marked regulator degree and quantum parameter
changes. It does not impose the filled-meridian condition above.
The proof here is disk lifting and flat area scaling; no invariant
identity is imported. The original source lower bound remains unproved.
